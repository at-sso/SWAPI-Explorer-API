"""
This software is provided "as is" without warranty of any kind, express or implied, including but not 
limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. 
In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, 
whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software 
or the use or other dealings in the software.
Copyright (c) 2024 zperk
"""

__all__ = [
    "load_file",
    "create_directory",
    "create_file",
    "delete_folder",
    "delete_folder_tree",
    "delete_oldest_files",
]

import os
import shutil
from datetime import datetime
from typing import Dict, Any, Union, Callable, List

from src.logger import *
from src.const import *


def __set_return_type(
    _object: Union[Any, Callable[..., Any]] = object,
    _content: str = "",
    is_error: bool = False,
) -> Dict[str, Union[object, str]]:
    """
    The function __set_return_type sets the return type and content for a function or object.

    @param _object The _object parameter in the __set_return_type function can be either any object
    or a callable function. It represents the return type of the function.
    @param _content The _content parameter in the __set_return_type function is a string that represents
    additional content related to the return type.

    @return The function __set_return_type returns a dictionary containing two keys:

    object, which holds the return type (_object), and
    content, which holds additional content (_content).
    If is_error is True, it returns an empty string for the content.
    """
    if is_error:
        return {"object": _object, "content": ""}
    return {"object": _object, "content": _content}


def load_file(absolute: str, mode: str = "r") -> Dict[str, Any]:
    """
    The function `load_file` opens a file and returns a dictionary containing the file object and its
    content, with error handling for file not found and unexpected errors.

    @param absolute The `absolute` parameter in the `load_file` function refers to the name or path of
    the file that you want to open and read. It is a required parameter for the function to work
    correctly. You need to provide the name or path of the file as a string when calling the `load
    @param mode The `mode` parameter in the `load_file` function specifies the mode in which the file
    should be opened. It is a string parameter with a default value of "r" which stands for reading
    mode.

    @return The function `load_file` returns a dictionary with keys 'object' and 'content' containing
    the file object opened in the specified mode and the content read from the file, respectively. If
    the file is not found, it returns an empty dictionary.
    """
    try:
        with open(absolute, mode) as file_object:
            file_contents: Any = file_object.read()
        logger.debug(f"File: {absolute} was loaded.")
        return __set_return_type(file_object, file_contents)
    except FileNotFoundError:
        logger.error(f"Directory of file '{absolute}' not found.")
        return __set_return_type(is_error=True)
    except Exception:
        logger_specials.unexpected_error(
            error_type="loading file",
            item=absolute,
        )
        return __set_return_type(is_error=True)


def create_directory(*args: str) -> None:
    """
    The function `create_directory` creates a directory if it does not already exist.

    @param directory The `directory` parameter in the `create_directory` function is a string that
    represents the path of the directory that needs to be created if it doesn't already exist.

    @return The function `create_directory` is returning `None`.
    """
    try:
        for directory in args:
            if not os.path.exists(directory):
                os.makedirs(directory)
                logger.info(f"Directory created: {directory}")
            else:
                logger.warning(f"Directory already exists: {directory}")
    except Exception as e:
        logger_specials.unexpected_error(
            error_type="creating directory",
            item=e,
        )


def create_file(*args: str) -> None:
    """
    The function `create_file` creates a file if it doesn't already exist, logging appropriate messages.

    @param file The `file` parameter in the `create_file` function represents the path of the file that
    needs to be created if it doesn't already exist.
    """
    try:
        for file in args:
            if not os.path.exists(file):
                file_loaded: Dict[Any, Any] = load_file(file, "w")
                file_loaded["object"].write("")
                logger.info(f"File created: {file}")
            else:
                logger.warning(f"File already exists: {file}")
    except Exception as e:
        logger_specials.unexpected_error(
            error_type="creating file",
            item=e,
        )


def delete_folder(*folders: str) -> None:
    """
    The `delete_folder` function deletes the specified folders along with their contents, if they exist.
    This function does not return any value (`None`). It logs information about the deletion process.
    If an error occurs during folder deletion, an error message is logged along with the traceback.

    @param *folders The `folders` parameter represents a variable number of folder names (as strings)
    that are to be deleted.
    """
    logger_specials.from_specific(
        name=__name__,
        func="delete_folder_tree",
        func_args=f"{folders}",
        message="was loaded.",
    )
    for current_component in folders:
        folder_path: str = os.path.join(ABSOLUTE_PATH, current_component)
        if os.path.exists(folder_path):
            try:
                shutil.rmtree(folder_path)
                logger.info(f"Deleted folder '{current_component}' at: {folder_path}.")
            except Exception:
                logger.error(
                    f"Error deleting folder '{current_component}' at: {folder_path}."
                )
        else:
            logger.warning(
                f"Folder '{current_component}' does not exist at: {folder_path}."
            )


def delete_folder_tree(*folders: str, init: str = "") -> None:
    """
    The function `delete_folder_tree` deletes the specified folders recursively from the file system.
    This function also logs the loading of the function using the provided folder names as arguments.

    Any existing folder specified in `folders` is recursively deleted. If a folder deletion operation fails,
    an error message is logged, including the traceback of the exception.
    If a specified folder does not exist, an error message is logged indicating the absence of the folder.

    @param folders The `folders` parameter is a variable-length argument representing the names of folders
    to be deleted. Each folder is specified as a string.
    @param init The `init` parameter is an optional string indicating the initial path where the deletion
    process should start. If not provided, the deletion process starts from the current working directory.
    """
    logger_specials.from_specific(
        name=__name__,
        func="delete_folder_tree",
        func_args=f"{folders}",
        message="was loaded.",
    )
    for root in os.walk(f"{ABSOLUTE_PATH}{init}", topdown=False):
        for current_component in folders:
            folder_path: str = os.path.join(root[0], current_component)
            if os.path.exists(folder_path):
                try:
                    shutil.rmtree(folder_path)
                    logger.info(
                        f"Deleted folder '{current_component}' at: {folder_path}."
                    )
                except Exception:
                    logger.error(
                        f"Error deleting folder '{current_component}' at: {folder_path}."
                    )
            else:
                logger.warning(
                    f"Folder '{current_component}' does not exist at: {folder_path}."
                )


def delete_oldest_files(path: str, max_tree: int = 10) -> None:
    """
    The function `delete_oldest_files` deletes the oldest files in a directory while keeping a maximum
    number of files specified by the `max_tree` parameter, handling any exceptions that may occur.

    @param path The `path` parameter in the `delete_oldest_files` function is a string representing the
    path to the directory where files will be deleted.

    @param max_tree The `max_tree` parameter in the `delete_oldest_files` function specifies the maximum
    number of files to keep in the directory. Its default value is `10`.

    @return None. This function does not return any value.

    In case of a `FileNotFoundError`, the function logs a warning indicating that the specified folder
    was not found. In case of any other exception, the function logs an error with a message containing
    information about the error that occurred.
    """
    try:
        # List all files in the directory
        files: List[str] = os.listdir(path)
        # Sort files based on their creation time
        files.sort(
            key=lambda K: datetime.strptime(K.split(".")[0], "%Y-%m-%d-%H-%M-%S")
        )

        # If the tree of files is less than `max_tree`, do nothing.
        if len(files) < max_tree:
            logger.info(f"Not enough files to delete ({max_tree}).")
            return

        # Calculate number of files to keep (1/10th of newest files)
        num_files_to_keep: int = max(len(files) // 10, 1)
        # Check if there are more files than the threshold
        if len(files) > num_files_to_keep:
            # Delete the oldest file(s)
            files_to_delete: List[str] = files[: len(files) - num_files_to_keep]
            for file_name in files_to_delete:
                file_path: str = os.path.join(path, file_name)
                os.remove(file_path)
                logger.warning(f"Deleted file: {file_path}")
    except FileNotFoundError:
        logger.warning(f"Folder '{path}' not found.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
