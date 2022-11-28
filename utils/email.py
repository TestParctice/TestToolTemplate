import re


def validate_email(email):
    """
    邮箱校验
    Args:
        email:
    Returns:
    """
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
        return True
    return False


if __name__ == '__main__':
    print(validate_email('sfas@qqcom'))
    print(validate_email('12312@qq.com'))
