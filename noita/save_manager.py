
import shutil

from loguru import logger
from pathlib import Path


class SaveManager:
    def __init__(self, saves_folder: Path, backups_folder: Path):
        self.saves_folder: Path = saves_folder
        self.backups_folder: Path = backups_folder

    @logger.catch
    def backup(self, backup_name: str, save_name: str = 'save00', overwrite: bool = False):
        logger.debug(f'Backing up save {save_name} to backup {backup_name} with overwrite={overwrite}')
        save_path: Path = self.saves_folder / save_name
        backup_path: Path = self.backups_folder / backup_name
        if backup_path.exists():
            if overwrite:
                logger.info('Removing existing backup...')
                shutil.rmtree(backup_path)
            else:
                raise FileExistsError(f'Backup {backup_name} already exists')
        logger.info('Copying save to backup...')
        shutil.copytree(
            src=save_path,
            dst=backup_path,
            dirs_exist_ok=overwrite,
        )

    @logger.catch
    def load(self, backup_name: str, save_name: str = 'save00', overwrite: bool = False):
        logger.debug(f'Loading backup {backup_name} to save {save_name} with overwrite={overwrite}')
        backup_path: Path = self.backups_folder / backup_name
        save_path: Path = self.saves_folder / save_name
        if overwrite:
            logger.info('Removing existing save...')
            shutil.rmtree(save_path)
        else:
            if save_path.exists():
                raise FileExistsError(f'Save {save_name} already exists')
        logger.info('Copying backup to save...')
        shutil.copytree(
            src=backup_path,
            dst=save_path,
            dirs_exist_ok=overwrite,
        )

