from src.db.repository import Repository


if __name__ == '__main__':
    r = Repository()
    rows = r.get_column("crude")
    for row in rows:
        print(row)