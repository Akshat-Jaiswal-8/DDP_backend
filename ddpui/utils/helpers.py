import shlex
import subprocess
import re
import string
import secrets


def runcmd(cmd, cwd):
    """runs a shell command in a specified working directory"""
    return subprocess.run(shlex.split(cmd), cwd=str(cwd), check=True)


def remove_nested_attribute(obj: dict, attr: str) -> dict:
    """
    this function searches for `attr` in the JSON object
    and removes any occurences it finds
    """
    if attr in obj:
        del obj[attr]

    for key in obj:
        val = obj[key]

        if isinstance(val, dict):
            obj[key] = remove_nested_attribute(val, attr)

        elif isinstance(val, list):
            for list_idx, list_val in enumerate(val):
                if isinstance(list_val, dict):
                    val[list_idx] = remove_nested_attribute(list_val, attr)

    return obj


def isvalid_email(email: str) -> bool:
    """
    this function uses a regex to check if the provided email
    address is valid
    ref: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    """
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    return re.fullmatch(regex, email)


def generate_hash_id(l: int) -> str:
    """
    this function generates a random hash id of length `l`
    """

    alphabet = string.ascii_lowercase + string.digits + string.ascii_uppercase

    return "".join(secrets.choice(alphabet) for _ in range(l))


def cleaned_name_for_prefectblock(blockname):
    """removes characters which are not lowercase letters, digits or dashes. same helper from prefect-proxy"""
    pattern = re.compile(r"[^\-a-z0-9]")
    return re.sub(pattern, "", blockname.lower())


def map_airbyte_keys_to_postgres_keys(conn_info: dict):
    """called by `post_system_transformation_tasks` and `_get_wclient`"""
    if "tunnel_method" in conn_info:
        method = conn_info["tunnel_method"]

        if method["tunnel_method"] in ["SSH_KEY_AUTH", "SSH_PASSWORD_AUTH"]:
            conn_info["ssh_host"] = method["tunnel_host"]
            conn_info["ssh_port"] = method["tunnel_port"]
            conn_info["ssh_username"] = method["tunnel_user"]

        if method["tunnel_method"] == "SSH_KEY_AUTH":
            conn_info["ssh_pkey"] = method["ssh_key"]
            conn_info["ssh_private_key_password"] = method.get(
                "tunnel_private_key_password"
            )

        elif method["tunnel_method"] == "SSH_PASSWORD_AUTH":
            conn_info["ssh_password"] = method.get("tunnel_user_password")

    conn_info["user"] = conn_info["username"]

    return conn_info
