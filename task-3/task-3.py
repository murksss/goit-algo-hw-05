from collections import defaultdict
import sys
from itertools import count


def parse_log_line(line: str) -> dict:
    """
    :param line: line from log file
    :return: parsed log line
    """
    try:
        split_line = line.split(' ')
        date = ' '.join(split_line[:2])
        level = split_line[2]
        message = ' '.join(split_line[3:])

        return dict(date=date, level=level, message=message)
    except IndexError as err:
        print('Something went wrong:', err)


def load_logs(file_path: str) -> list:
    """
    :param file_path: path to log file
    :return: list of parsed log lines
    """
    try:
        with open(file_path, 'r') as f:
            lines = [el.strip() for el in f.readlines()]

        return [parse_log_line(line) for line in lines]
    except FileNotFoundError as err:
        print('Something went wrong:', err)


def filter_logs_by_level(_logs: list, _level: str) -> list:
    """
    :param _logs: list of parsed log lines
    :param _level: level of log
    :return: list of log lines filtered by level
    """
    return list(filter(lambda _log: _log['level'].upper() == _level.upper(), _logs))


def count_logs_by_level(_logs: list) -> dict:
    """
    :param _logs: list of parsed log lines
    :return: dictionary of counts of log lines filtered by level
    """
    level_counts = defaultdict(int)
    for _log in _logs:
        level_counts[_log['level']] += 1

    return level_counts


def display_log_counts(_counts: dict) -> None:
    """
    :param _counts: dictionary of counts of log lines filtered by level

    Display info about counts of log lines filtered by level in tabular format
    """
    if not _counts:
        print('No log counts')
        return None

    print(f'{"Level":<10} | {"Count":<10}')
    print(f'{"-"*10} | {"-"*10}')
    for _level, _count in _counts.items():
        print(f'{_level:<10} | {_count:<10}')


def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        logs = load_logs(file_path=file_path)
        counts = count_logs_by_level(_logs=logs)
        display_log_counts(_counts=counts)
        if len(sys.argv) > 2:
            level = sys.argv[2]
            filtered_logs = filter_logs_by_level(_logs=logs, _level=level)
            if filtered_logs:
                print(f'\nFiltered log by level: {level.upper()}')
                for filtered_log in filtered_logs:
                    print(f"{filtered_log['date']}: {filtered_log['message']}")
            else:
                print(f'\nNo logs filtered by level: {level.upper()}')
    else:
        print('Usage: python task-3.py <file_path> <level>')


if __name__ == '__main__':
    main()
