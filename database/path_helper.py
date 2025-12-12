import os

def get_db_path(db_filename="ecommerce.db"):
    utils_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.normpath(os.path.join(utils_dir, ".."))
    db_path = os.path.join(project_root, db_filename)
    return db_path
