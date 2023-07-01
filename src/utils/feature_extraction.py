from password_strength import PasswordStats


def cal_strength(text: str) -> int:
    return PasswordStats(text).strength()

