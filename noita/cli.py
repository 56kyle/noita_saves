import click
import time

from loguru import logger
from pathlib import Path

from noita.save_manager import SaveManager


SAVES_FOLDER: Path = Path(r'C:\Users\56kyl\AppData\LocalLow\Nolla_Games_Noita')
BACKUPS_FOLDER: Path = Path(r'C:\Users\56kyl\Desktop\noita backups')
QUICKSAVES_FOLDER: Path = Path(r'C:\Users\56kyl\Desktop\noita quicksaves')


@click.command()
@click.argument('backup_name')
@click.argument('save_name', required=False, default='save00')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing files')
def load(backup_name, save_name, force):
    logger.info(f'Loading backup from {backup_name} to {save_name} with force={force}...')
    save_manager = SaveManager(
        saves_folder=SAVES_FOLDER,
        backups_folder=BACKUPS_FOLDER,
    )
    save_manager.load(backup_name=backup_name, save_name=save_name, overwrite=force)
    logger.info('...Done')


@click.command()
@click.argument('backup_name')
@click.argument('save_name', required=False, default='save00')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing files')
def backup(backup_name, save_name, force):
    logger.info(f'Backing up from {save_name} to {backup_name} with force={force}...')
    save_manager = SaveManager(
        saves_folder=SAVES_FOLDER,
        backups_folder=BACKUPS_FOLDER,
    )
    save_manager.backup(backup_name=backup_name, save_name=save_name, overwrite=force)
    logger.info('...Done')


@click.command()
def quicksave():
    logger.info('Quicksaving...')
    save_manager = SaveManager(
        saves_folder=SAVES_FOLDER,
        backups_folder=QUICKSAVES_FOLDER,
    )
    save_manager.backup(backup_name=str(time.time_ns()), save_name='save00', overwrite=True)
    logger.info('...Done')


@click.command()
def quickload():
    logger.info('Quickloading...')
    save_manager = SaveManager(
        saves_folder=SAVES_FOLDER,
        backups_folder=QUICKSAVES_FOLDER,
    )

    most_recent_path_time: int = 0
    most_recent_path = None
    for path in QUICKSAVES_FOLDER.iterdir():
        if int(path.name) > most_recent_path_time:
            most_recent_path = path
    if most_recent_path is None:
        raise FileNotFoundError('No quicksave found')

    save_manager.load(backup_name=most_recent_path.name, save_name='save00', overwrite=True)
    logger.info('...Done')


@click.command()
def list():
    logger.info(r'Backups in {backups_folder}:')
    for backup_name in BACKUPS_FOLDER.iterdir():
        logger.info(f'\t{backup_name}')

