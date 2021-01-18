import reapy
from reapy import reascript_api as RPR
from reapy.core import ReapyObject
import typing as ty


class Item(ReapyObject):

    _class_name = "Item"
    id: str

    def __init__(self, id: str) -> None:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    @property
    def _args(self) -> ty.Tuple[str]:
        ...

    @property
    def active_take(self) -> reapy.Take:
        """
        Return the active take of the item.

        Returns
        -------
        take : Take
            Active take of the item.
        """
        ...

    def add_take(self) -> reapy.Take:
        """
        Create and return a new take in item.

        Returns
        -------
        take : Take
            New take in item.
        """
        ...

    def delete(self) -> None:
        """Delete item."""
        ...

    def get_info_value(self, param_name: str) -> float:
        ...

    def get_take(self, index: int) -> reapy.Take:
        """
        Return index-th take of item.

        Parameters
        ----------
        index : int
            Take index.

        Returns
        -------
        take : Take
            index-th take of media item.
        """
        ...

    @property
    def has_valid_id(self) -> bool:
        """
        Whether ReaScript ID is still valid.

        For instance, if item has been deleted, ID will not be valid
        anymore.

        :type: bool
        """

    @property
    def is_selected(self) -> bool:
        """
        Return whether item is selected.

        Returns
        -------
        is_selected : bool
            Whether item is selected.
        """
        ...

    @is_selected.setter
    def is_selected(self, value: bool) -> None:
        ...

    @property
    def length(self) -> float:
        """
        Return item length in seconds.

        Returns
        -------
        length : float
            Item length in seconds.
        """
        ...

    @length.setter
    def length(self, length: float) -> None:
        """
        Set item length.

        Parameters
        ----------
        length : float
            New item length in seconds.
        """
        ...

    def make_only_selected_item(self) -> None:
        """
        Make track the only selected item in parent project.
        """
        ...

    @property
    def n_takes(self) -> int:
        """
        Return the number of takes of media item.

        Returns
        -------
        n_takes : int
            Number of takes of media item.
        """
        ...

    @property
    def position(self) -> float:
        """
        Return item position in seconds.

        Returns
        -------
        position : float
            Item position in seconds.
        """
        ...

    @position.setter
    def position(self, position: float) -> None:
        """
        Set media item position to `position`.

        Parameters
        ----------
        position : float
            New item position in seconds.
        """
        ...

    @property
    def project(self) -> reapy.Project:
        """
        Return item parent project.

        Returns
        -------
        project : Project
            Item parent project.
        """
        ...

    def set_info_value(self, param_name: str, value: float) -> None:
        """
        Set raw item info value.

        Parameters
        ----------
        param_name : str
        value : float
        """

    def split(self, position: float) -> ty.Tuple[Item, Item]:
        """
        Split item and return left and right parts.

        Parameters
        ----------
        position : float
            Split position in seconds.

        Returns
        -------
        left, right : Item
            Left and right parts of the split.
        """
        ...

    @property
    def takes(self) -> ty.List[reapy.Take]:
        """
        Return list of all takes of media item.

        Returns
        -------
        takes : list of Take
            List of all takes of media item.
        """
        ...

    @property
    def track(self) -> reapy.Track:
        """
        Parent track of item.

        Set it by passing a track, or a track index.

        :type: Track

        Examples
        --------
        >>> track0, track1 = project.tracks[0:2]
        >>> item = track0.items[0]
        >>> item.track == track0
        True
        >>> item.track = track1  # Move to track 1
        >>> item.track = 0  # Move to track 0
        """
        ...

    @track.setter
    def track(self, track: ty.Union[int, reapy.Track]) -> None:
        ...

    def update(self) -> None:
        """Update item in REAPER interface."""
        ...
