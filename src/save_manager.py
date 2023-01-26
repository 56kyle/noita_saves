
import os
import shutil

from loguru import logger


class SaveManager:
    def __init__(self, saves_folder: str, backups_folder: str):
        self.saves_folder = saves_folder
        self.backups_folder = backups_folder

    def backup(self, backup_name: str, save_name: str = 'save00', overwrite: bool = False):
        logger.debug(f'Backing up save {save_name} to backup {backup_name} with overwrite={overwrite}')
        save_path: str = os.path.join(self.saves_folder, save_name)
        backup_path: str = os.path.join(self.backups_folder, backup_name)
        if os.path.exists(backup_path):
            if overwrite:
                print('Removing existing backup...')
                shutil.rmtree(backup_path)
            else:
                raise FileExistsError(f'Backup {backup_name} already exists')
        shutil.copytree(
            src=save_path,
            dst=backup_path,
            dirs_exist_ok=overwrite,
        )

    def load(self, backup_name: str, save_name: str = 'save00', overwrite: bool = False):
        logger.debug(f'Loading backup {backup_name} to save {save_name} with overwrite={overwrite}')
        backup_path: str = os.path.join(self.backups_folder, backup_name)
        save_path: str = os.path.join(self.saves_folder, save_name)
        if overwrite:
            print('Removing existing save...')
            shutil.rmtree(save_path)
        else:
            if os.path.exists(save_path):
                raise FileExistsError(f'Save {save_name} already exists')
        shutil.copytree(
            src=backup_path,
            dst=save_path,
            dirs_exist_ok=overwrite,
        )

