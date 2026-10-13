"""Пример программы для учебного репозитория Space."""


def count_commits(log_lines):
    """Возвращает количество коммитов в выводе git log --oneline."""
    return len([line for line in log_lines if line.strip()])


if __name__ == "__main__":
    history = ["a1b2c3d Add files via upload", "4e5f6a7 Create README.md"]
    print(f"Коммитов в истории: {count_commits(history)}")
