"""A command parser class."""

import textwrap
from typing import Sequence


class CommandException(Exception):
    """A class used to represent a wrong command exception."""
    pass


class CommandParser:
    """A class used to parse and execute a user Command."""

    def __init__(self, video_player):
        self._player = video_player

    def execute_command(self, command: Sequence[str]):
        """Executes the user command. Expects the command to be upper case.
           Raises CommandException if a command cannot be parsed.
        """
        if not command:
            raise CommandException(
                "Please enter a valid command, "
                "type HELP for a list of available commands.")

        if command[0].upper() == "NUMBER_OF_VIDEOS":
            self._player.number_of_videos()

        elif command[0].upper() == "SHOW_ALL_VIDEOS":
            self._player.show_all_videos()

        elif command[0].upper() == "PLAY":
            if len(command) != 2:
                raise CommandException(
                    "Please enter PLAY command followed by video_id.")
            self._player.play_video(command[1])

        elif command[0].upper() == "PLAY_RANDOM":
            self._player.play_random_video()

        elif command[0].upper() == "STOP":
            self._player.stop_video()

        elif command[0].upper() == "PAUSE":
            self._player.pause_video()

        elif command[0].upper() == "CONTINUE":
            self._player.continue_video()

        elif command[0].upper() == "SHOW_PLAYING":
            self._player.show_playing()

        elif command[0].upper() == "CREATE_PLAYLIST":
            if len(command) != 2:
                raise CommandException(
                    "Please enter CREATE_PLAYLIST command followed by a "
                    "playlist name.")
            self._player.create_playlist(command[1])

        elif command[0].upper() == "ADD_TO_PLAYLIST":
            if len(command) != 3:
                raise CommandException(
                    "Please enter ADD_TO_PLAYLIST command followed by a "
                    "playlist name and video_id to add.")
            self._player.add_to_playlist(command[1], command[2])

        elif command[0].upper() == "REMOVE_FROM_PLAYLIST":
            if len(command) != 3:
                raise CommandException(
                    "Please enter REMOVE_FROM_PLAYLIST command followed by a "
                    "playlist name and video_id to remove.")
            self._player.remove_from_playlist(command[1], command[2])

        elif command[0].upper() == "CLEAR_PLAYLIST":
            if len(command) != 2:
                raise CommandException(
                    "Please enter CLEAR_PLAYLIST command followed by a "
                    "playlist name.")
            self._player.clear_playlist(command[1])

        elif command[0].upper() == "DELETE_PLAYLIST":
            if len(command) != 2:
                raise CommandException(
                    "Please enter DELETE_PLAYLIST command followed by a "
                    "playlist name.")
            self._player.delete_playlist(command[1])

        elif command[0].upper() == "SHOW_PLAYLIST":
            if len(command) != 2:
                raise CommandException(
                    "Please enter SHOW_PLAYLIST command followed by a "
                    "playlist name.")
            self._player.show_playlist(command[1])

        elif command[0].upper() == "SHOW_ALL_PLAYLISTS":
            self._player.show_all_playlists()

        elif command[0].upper() == "SEARCH_VIDEOS":
            if len(command) != 2:
                raise CommandException(
                    "Please enter SEARCH_VIDEOS command followed by a "
                    "search term.")
            self._player.search_videos(command[1])

        elif command[0].upper() == "SEARCH_VIDEOS_WITH_TAG":
            if len(command) != 2:
                raise CommandException(
                    "Please enter SEARCH_VIDEOS_WITH_TAG command followed by a "
                    "video tag.")
            self._player.search_videos_tag(command[1])

        elif command[0].upper() == "FLAG_VIDEO":
            if len(command) == 3:
                self._player.flag_video(command[1], command[2])
            elif len(command) == 2:
                self._player.flag_video(command[1])
            else:
                raise CommandException(
                    "Please enter FLAG_VIDEO command followed by a "
                    "video_id and an optional flag reason.")

        elif command[0].upper() == "ALLOW_VIDEO":
            if len(command) != 2:
                raise CommandException(
                    "Please enter ALLOW_VIDEO command followed by a "
                    "video_id.")
            self._player.allow_video(command[1])

        elif command[0].upper() == "HELP":
            self._get_help()
        else:
            print(
                "Please enter a valid command, type HELP for a list of "
                "available commands.")

    def _get_help(self):
        """Displays all available commands to the user."""
        help_text = textwrap.dedent("""
        Available commands:
            NUMBER_OF_VIDEOS - Shows how many videos are in the library.
            SHOW_ALL_VIDEOS - Lists all videos from the library.
            PLAY <video_id> - Plays specified video.
            PLAY_RANDOM - Plays a random video from the library.
            STOP - Stop the current video.
            PAUSE - Pause the current video.
            CONTINUE - Resume the current paused video.
            SHOW_PLAYING - Displays the title, url and paused status of the video that is currently playing (or paused).
            CREATE_PLAYLIST <playlist_name> - Creates a new (empty) playlist with the provided name.
            ADD_TO_PLAYLIST <playlist_name> <video_id> - Adds the requested video to the playlist.
            REMOVE_FROM_PLAYLIST <playlist_name> <video_id> - Removes the specified video from the specified playlist
            CLEAR_PLAYLIST <playlist_name> - Removes all the videos from the playlist.
            DELETE_PLAYLIST <playlist_name> - Deletes the playlist.
            SHOW_PLAYLIST <playlist_name> - List all the videos in this playlist.
            SHOW_ALL_PLAYLISTS - Display all the available playlists.
            SEARCH_VIDEOS <search_term> - Display all the videos whose titles contain the search_term.
            SEARCH_VIDEOS_WITH_TAG <tag_name> -Display all videos whose tags contains the provided tag.
            FLAG_VIDEO <video_id> <flag_reason> - Mark a video as flagged.
            ALLOW_VIDEO <video_id> - Removes a flag from a video.
            HELP - Displays help.
            EXIT - Terminates the program execution.
        """)
        print(help_text)
        """A youtube terminal simulator."""
        from .video_player import VideoPlayer
        from .command_parser import CommandException
        from .command_parser import CommandParser

        if __name__ == "__main__":
            print("""Hello and welcome to YouTube, what would you like to do?
            Enter HELP for list of available commands or EXIT to terminate.""")
            video_player = VideoPlayer()
            parser = CommandParser(video_player)
            while True:
                command = input("YT> ")
                if command.upper() == "EXIT":
                    break
                try:
                    parser.execute_command(command.split())
                except CommandException as e:
                    print(e)
            print("YouTube has now terminated its execution. "
                  "Thank you and goodbye!")
            """A video class."""

            from typing import Sequence

            class Video:
                """A class used to represent a Video."""

                def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
                    """Video constructor."""
                    self._title = video_title
                    self._video_id = video_id

                    # Turn the tags into a tuple here so it's unmodifiable,
                    # in case the caller changes the 'video_tags' they passed to us
                    self._tags = tuple(video_tags)

                @property
                def title(self) -> str:
                    """Returns the title of a video."""
                    return self._title

                @property
                def video_id(self) -> str:
                    """Returns the video id of a video."""
                    return self._video_id

                @property
                def tags(self) -> Sequence[str]:
                    """Returns the list of tags of a video."""
                    return self._tags

                """A video library class."""

                from .video import Video
                from pathlib import Path
                import csv

                # Helper Wrapper around CSV reader to strip whitespace from around
                # each item.
                def _csv_reader_with_strip(reader):
                    yield from ((item.strip() for item in line) for line in reader)

                class VideoLibrary:
                    """A class used to represent a Video Library."""

                    def __init__(self):
                        """The VideoLibrary class is initialized."""
                        self._videos = {}
                        with open(Path(__file__).parent / "videos.txt") as video_file:
                            reader = _csv_reader_with_strip(
                                csv.reader(video_file, delimiter="|"))
                            for video_info in reader:
                                title, url, tags = video_info
                                self._videos[url] = Video(
                                    title,
                                    url,
                                    [tag.strip() for tag in tags.split(",")] if tags else [],
                                )

                    def get_all_videos(self):
                        """Returns all available video information from the video library."""
                        return list(self._videos.values())

                    def get_video(self, video_id):
                        """Returns the video object (title, url, tags) from the video library.
                        Args:
                            video_id: The video url.
                        Returns:
                            The Video object for the requested video_id. None if the video
                            does not exist.
                        """
                        return self._videos.get(video_id, None)

                    """A video player class."""

                    from .video_library import VideoLibrary

                    class VideoPlayer:
                        """A class used to represent a Video Player."""

                        def __init__(self):
                            self._video_library = VideoLibrary()

                        def number_of_videos(self):
                            num_videos = len(self._video_library.get_all_videos())
                            print(f"{num_videos} videos in the library")

                        def show_all_videos(self):
                            """Returns all videos."""

                            print("show_all_videos needs implementation")

                        def play_video(self, video_id):
                            """Plays the respective video.
                            Args:
                                video_id: The video_id to be played.
                            """
                            print("play_video needs implementation")

                        def stop_video(self):
                            """Stops the current video."""

                            print("stop_video needs implementation")

                        def play_random_video(self):
                            """Plays a random video from the video library."""

                            print("play_random_video needs implementation")

                        def pause_video(self):
                            """Pauses the current video."""

                            print("pause_video needs implementation")

                        def continue_video(self):
                            """Resumes playing the current video."""

                            print("continue_video needs implementation")

                        def show_playing(self):
                            """Displays video currently playing."""

                            print("show_playing needs implementation")

                        def create_playlist(self, playlist_name):
                            """Creates a playlist with a given name.
                            Args:
                                playlist_name: The playlist name.
                            """
                            print("create_playlist needs implementation")

                        def add_to_playlist(self, playlist_name, video_id):
                            """Adds a video to a playlist with a given name.
                            Args:
                                playlist_name: The playlist name.
                                video_id: The video_id to be added.
                            """
                            print("add_to_playlist needs implementation")

                        def show_all_playlists(self):
                            """Display all playlists."""

                            print("show_all_playlists needs implementation")

                        def show_playlist(self, playlist_name):
                            """Display all videos in a playlist with a given name.
                            Args:
                                playlist_name: The playlist name.
                            """
                            print("show_playlist needs implementation")

                        def remove_from_playlist(self, playlist_name, video_id):
                            """Removes a video to a playlist with a given name.
                            Args:
                                playlist_name: The playlist name.
                                video_id: The video_id to be removed.
                            """
                            print("remove_from_playlist needs implementation")

                        def clear_playlist(self, playlist_name):
                            """Removes all videos from a playlist with a given name.
                            Args:
                                playlist_name: The playlist name.
                            """
                            print("clears_playlist needs implementation")

                        def delete_playlist(self, playlist_name):
                            """Deletes a playlist with a given name.
                            Args:
                                playlist_name: The playlist name.
                            """
                            print("deletes_playlist needs implementation")

                        def search_videos(self, search_term):
                            """Display all the videos whose titles contain the search_term.
                            Args:
                                search_term: The query to be used in search.
                            """
                            print("search_videos needs implementation")

                        def search_videos_tag(self, video_tag):
                            """Display all videos whose tags contains the provided tag.
                            Args:
                                video_tag: The video tag to be used in search.
                            """
                            print("search_videos_tag needs implementation")

                        def flag_video(self, video_id, flag_reason=""):
                            """Mark a video as flagged.
                            Args:
                                video_id: The video_id to be flagged.
                                flag_reason: Reason for flagging the video.
                            """
                            print("flag_video needs implementation")

                        def allow_video(self, video_id):
                            """Removes a flag from a video.
                            Args:
                                video_id: The video_id to be allowed again.
                            """
                            print("allow_video needs implementation")
                            """A video playlist class."""

                            class Playlist:
                                """A class used to represent a Playlist."""
                                import re
                                from src.video_player import VideoPlayer

                                def test_number_of_videos(capfd):
                                    player = VideoPlayer()
                                    player.number_of_videos()
                                    out, err = capfd.readouterr()
                                    assert "5 videos in the library" in out

                                def test_show_all_videos(capfd):
                                    player = VideoPlayer()
                                    player.show_all_videos()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 6
                                    assert "Here's a list of all available videos:" in lines[0]
                                    assert "Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[1]
                                    assert "Another Cat Video (another_cat_video_id) [#cat #animal]" in lines[2]
                                    assert "Funny Dogs (funny_dogs_video_id) [#dog #animal]" in lines[3]
                                    assert "Life at Google (life_at_google_video_id) [#google #career]" in lines[4]
                                    assert "Video about nothing (nothing_video_id) []" in lines[5]

                                def test_play_video(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 1
                                    assert "Playing video: Amazing Cats" in out

                                def test_play_video_nonexistent(capfd):
                                    player = VideoPlayer()
                                    player.play_video("does_not_exist")
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 1
                                    assert "Cannot play video: Video does not exist" in out

                                def test_play_video_stop_previous(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.play_video("funny_dogs_video_id")
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 3
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Stopping video: Amazing Cats" in lines[1]
                                    assert "Playing video: Funny Dogs" in lines[2]

                                def test_play_video_dont_stop_previous_if_nonexistent(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.play_video("some_other_video")
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 2
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Stopping video: Amazing Cats" not in out
                                    assert "Cannot play video: Video does not exist" in lines[1]

                                def test_stop_video(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.stop_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 2
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Stopping video: Amazing Cats" in lines[1]

                                def test_stop_video_twice(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.stop_video()
                                    player.stop_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 3
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Stopping video: Amazing Cats" in lines[1]
                                    assert "Cannot stop video: No video is currently playing" in lines[2]

                                def test_stop_video_none_playing(capfd):
                                    player = VideoPlayer()
                                    player.stop_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 1
                                    assert "Cannot stop video: No video is currently playing" in out

                                def test_play_random_video(capfd):
                                    player = VideoPlayer()
                                    player.play_random_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 1
                                    assert re.match(
                                        "Playing video: (Amazing Cats|Another Cat Video|Funny Dogs|Life at Google|Video about nothing)",
                                        out)

                                def test_play_random_stops_previous_video(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.play_random_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 3
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Stopping video: Amazing Cats" in lines[1]
                                    assert re.match(
                                        "Playing video: (Amazing Cats|Another Cat Video|Funny Dogs|Life at Google|Video about nothing)",
                                        lines[2])

                                def test_show_playing(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.show_playing()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 2
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Currently playing: Amazing Cats (amazing_cats_video_id) [#cat #animal]" in \
                                           lines[1]

                                def test_show_nothing_playing(capfd):
                                    player = VideoPlayer()
                                    player.show_playing()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 1
                                    assert "No video is currently playing" in lines[0]

                                def test_pause_video(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.pause_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 2
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Pausing video: Amazing Cats" in lines[1]

                                def test_pause_video_show_playing(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.pause_video()
                                    player.show_playing()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 3
                                    assert "Currently playing: Amazing Cats (amazing_cats_video_id) " \
                                           "[#cat #animal] - PAUSED" in lines[2]

                                def test_pause_video_play_video(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.pause_video()
                                    player.play_video("amazing_cats_video_id")
                                    player.show_playing()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 5
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Pausing video: Amazing Cats" in lines[1]
                                    assert "Stopping video: Amazing Cats" in lines[2]
                                    assert "Playing video: Amazing Cats" in lines[3]
                                    assert "Currently playing: Amazing Cats (amazing_cats_video_id) " \
                                           "[#cat #animal]" in lines[4]
                                    assert "PAUSED" not in lines[4]

                                def test_pause_already_paused_video(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.pause_video()
                                    player.pause_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 3
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Pausing video: Amazing Cats" in lines[1]
                                    assert "Video already paused: Amazing Cats" in lines[2]

                                def test_pause_video_none_playing(capfd):
                                    player = VideoPlayer()
                                    player.pause_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 1
                                    assert "Cannot pause video: No video is currently playing" in lines[0]

                                def test_continue_video(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.pause_video()
                                    player.continue_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 3
                                    assert "Playing video: Amazing Cats" in lines[0]
                                    assert "Pausing video: Amazing Cats" in lines[1]
                                    assert "Continuing video: Amazing Cats" in lines[2]

                                def test_continue_video_not_paused(capfd):
                                    player = VideoPlayer()
                                    player.play_video("amazing_cats_video_id")
                                    player.continue_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 2
                                    assert "Cannot continue video: Video is not paused" in lines[1]

                                def test_continue_none_playing(capfd):
                                    player = VideoPlayer()
                                    player.continue_video()
                                    out, err = capfd.readouterr()
                                    lines = out.splitlines()
                                    assert len(lines) == 1
                                    assert "Cannot continue video: No video is currently playing" in lines[0]
                                    from src.video_player import VideoPlayer

                                    def test_create_playlist(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_PLAYlist")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 1
                                        assert "Successfully created new playlist: my_PLAYlist" in lines[0]

                                    def test_create_existing_playlist(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.create_playlist("my_COOL_PLAYLIST")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 2
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert ("Cannot create playlist: A playlist with the same name already "
                                                "exists") in lines[1]

                                    def test_add_to_playlist(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_COOL_playlist")
                                        player.add_to_playlist("my_cool_PLAYLIST", "amazing_cats_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 2
                                        assert "Successfully created new playlist: my_COOL_playlist" in lines[0]
                                        assert "Added video to my_cool_PLAYLIST: Amazing Cats" in lines[1]

                                    def test_add_to_playlist_already_added(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.add_to_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        player.add_to_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 3
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert "Added video to my_cool_playlist: Amazing Cats" in lines[1]
                                        assert "Cannot add video to my_cool_playlist: Video already added" in lines[2]

                                    def test_add_to_playlist_nonexistent_video(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.add_to_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        player.add_to_playlist("my_cool_playlist", "some_other_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 3
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert "Added video to my_cool_playlist: Amazing Cats" in lines[1]
                                        assert "Cannot add video to my_cool_playlist: Video does not exist" in lines[2]

                                    def test_add_to_playlist_nonexistent_playlist(capfd):
                                        player = VideoPlayer()
                                        player.add_to_playlist("another_playlist", "amazing_cats_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 1
                                        assert "Cannot add video to another_playlist: Playlist does not exist" in lines[
                                            0]

                                    def test_add_to_playlist_nonexistent_playlist_nonexistent_video(capfd):
                                        player = VideoPlayer()
                                        player.add_to_playlist("another_playlist", "does_not_exist_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 1
                                        assert "Cannot add video to another_playlist: Playlist does not exist" in lines[
                                            0]

                                    def test_show_all_playlists_no_playlists_exist(capfd):
                                        player = VideoPlayer()
                                        player.show_all_playlists()
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 1
                                        assert "No playlists exist yet" in lines[0]

                                    def test_show_all_playlists(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playLIST")
                                        player.create_playlist("anotheR_playlist")
                                        player.show_all_playlists()
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 5
                                        assert "Showing all playlists:" in lines[2]
                                        assert "anotheR_playlist" in lines[3]
                                        assert "my_cool_playLIST" in lines[4]

                                    def test_show_playlist(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.show_playlist("my_cool_playlist")
                                        player.add_to_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        player.show_playlist("my_COOL_playlist")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 6
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert "Showing playlist: my_cool_playlist" in lines[1]
                                        assert "No videos here yet" in lines[2]
                                        assert "Added video to my_cool_playlist: Amazing Cats" in lines[3]
                                        assert "Showing playlist: my_COOL_playlist" in lines[4]
                                        assert "Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[5]

                                    def test_remove_from_playlist_then_re_add(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("MY_playlist")
                                        player.add_to_playlist("my_playlist", "amazing_cats_video_id")
                                        player.add_to_playlist("my_playlist", "life_at_google_video_id")
                                        player.remove_from_playlist("my_playlist", "amazing_cats_video_id")
                                        player.add_to_playlist("my_playlist", "amazing_cats_video_id")
                                        player.show_playlist("my_playLIST")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 8
                                        assert "Showing playlist: my_playLIST" in lines[5]
                                        assert "Life at Google (life_at_google_video_id) [#google #career]" in lines[6]
                                        assert "Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[7]

                                    def test_show_playlist_nonexistent_playlist(capfd):
                                        player = VideoPlayer()
                                        player.show_playlist("another_playlist")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 1
                                        assert "Cannot show playlist another_playlist: Playlist does not exist" in \
                                               lines[0]

                                    def test_remove_from_playlist(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.add_to_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        player.remove_from_playlist("my_COOL_playlist", "amazing_cats_video_id")
                                        player.remove_from_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 4
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert "Added video to my_cool_playlist: Amazing Cats" in lines[1]
                                        assert "Removed video from my_COOL_playlist: Amazing Cats" in lines[2]
                                        assert "Cannot remove video from my_cool_playlist: Video is not in playlist" in \
                                               lines[3]

                                    def test_remove_from_playlist_video_is_not_in_playlist(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.remove_from_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 2
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert "Cannot remove video from my_cool_playlist: Video is not in playlist" in \
                                               lines[1]

                                    def test_remove_from_playlist_nonexistent_video(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.add_to_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        player.remove_from_playlist("my_cool_playlist", "some_other_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 3
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert "Added video to my_cool_playlist: Amazing Cats" in lines[1]
                                        assert "Cannot remove video from my_cool_playlist: Video does not exist" in \
                                               lines[2]

                                    def test_remove_from_playlist_nonexistent_playlist(capfd):
                                        player = VideoPlayer()
                                        player.remove_from_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 1
                                        assert "Cannot remove video from my_cool_playlist: Playlist does not exist" in \
                                               lines[0]

                                    def test_clear_playlist(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.add_to_playlist("my_cool_playlist", "amazing_cats_video_id")
                                        player.show_playlist("my_cool_playlist")
                                        player.clear_playlist("my_COOL_playlist")
                                        player.show_playlist("my_cool_playlist")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 7
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert "Added video to my_cool_playlist: Amazing Cats" in lines[1]
                                        assert "Showing playlist: my_cool_playlist" in lines[2]
                                        assert "Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[3]
                                        assert "Successfully removed all videos from my_COOL_playlist" in lines[4]
                                        assert "Showing playlist: my_cool_playlist" in lines[5]
                                        assert "No videos here yet" in lines[6]

                                    def test_clear_playlist_nonexistent(capfd):
                                        player = VideoPlayer()
                                        player.clear_playlist("my_cool_playlist")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 1
                                        assert "Cannot clear playlist my_cool_playlist: Playlist does not exist" in \
                                               lines[0]

                                    def test_delete_playlist(capfd):
                                        player = VideoPlayer()
                                        player.create_playlist("my_cool_playlist")
                                        player.delete_playlist("my_cool_playlist")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 2
                                        assert "Successfully created new playlist: my_cool_playlist" in lines[0]
                                        assert "Deleted playlist: my_cool_playlist" in lines[1]

                                    def test_delete_playlist_nonexistent(capfd):
                                        player = VideoPlayer()
                                        player.delete_playlist("my_cool_playlist")
                                        out, err = capfd.readouterr()
                                        lines = out.splitlines()
                                        assert len(lines) == 1
                                        assert "Cannot delete playlist my_cool_playlist: Playlist does not exist" in \
                                               lines[0]
                                        from src.video_player import VideoPlayer
                                        from unittest import mock

                                        @mock.patch('builtins.input', lambda *args: 'No')
                                        def test_search_videos_with_no_answer(capfd):
                                            player = VideoPlayer()
                                            player.search_videos("cat")
                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 5
                                            assert "Here are the results for cat:" in lines[0]
                                            assert "1) Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[1]
                                            assert "2) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                   lines[2]
                                            assert ("Would you like to play any of the above? If yes, "
                                                    "specify the number of the video.") in lines[3]
                                            assert (
                                                       "If your answer is not a valid number, we will assume "
                                                       "it's a no.") in lines[4]
                                            assert "Playing video" not in out

                                        @mock.patch('builtins.input', lambda *args: '2')
                                        def test_search_videos_and_play_answer(capfd):
                                            player = VideoPlayer()
                                            player.search_videos("cat")

                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 6
                                            assert "Here are the results for cat:" in lines[0]
                                            assert "1) Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[1]
                                            assert "2) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                   lines[2]
                                            assert ("Would you like to play any of the above? If yes, "
                                                    "specify the number of the video.") in lines[3]
                                            assert ("If your answer is not a valid number, we will assume "
                                                    "it's a no.") in lines[4]
                                            assert "Playing video: Another Cat Video" in lines[5]

                                        @mock.patch('builtins.input', lambda *args: '6')
                                        def test_search_videos_number_out_of_bounds(capfd):
                                            player = VideoPlayer()
                                            player.search_videos("cat")

                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 5
                                            assert "Here are the results for cat:" in lines[0]
                                            assert "1) Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[1]
                                            assert "2) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                   lines[2]
                                            assert ("Would you like to play any of the above? If yes, "
                                                    "specify the number of the video.") in lines[3]
                                            assert ("If your answer is not a valid number, we will assume "
                                                    "it's a no.") in lines[4]
                                            assert "Playing video" not in out

                                        @mock.patch('builtins.input', lambda *args: 'ab3g')
                                        def test_search_videos_invalid_number(capfd):
                                            player = VideoPlayer()
                                            player.search_videos("cat")

                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 5
                                            assert "Here are the results for cat:" in lines[0]
                                            assert "1) Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[1]
                                            assert "2) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                   lines[2]
                                            assert ("Would you like to play any of the above? If yes, "
                                                    "specify the number of the video.") in lines[3]
                                            assert ("If your answer is not a valid number, we will assume "
                                                    "it's a no.") in lines[4]
                                            assert "Playing video" not in out

                                        def test_search_videos_no_results(capfd):
                                            player = VideoPlayer()
                                            player.search_videos("blah")
                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 1
                                            assert "No search results for blah" in lines[0]

                                        @mock.patch('builtins.input', lambda *args: 'No')
                                        def test_search_videos_with_tag_no_answer(capfd):
                                            player = VideoPlayer()
                                            player.search_videos_tag("#cat")
                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 5
                                            assert "Here are the results for #cat:" in lines[0]
                                            assert "1) Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[1]
                                            assert "2) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                   lines[2]
                                            assert ("Would you like to play any of the above? If yes, "
                                                    "specify the number of the video.") in lines[3]
                                            assert ("If your answer is not a valid number, we will assume "
                                                    "it's a no.") in lines[4]

                                        @mock.patch('builtins.input', lambda *args: '1')
                                        def test_search_videos_with_tag_play_answered_number(capfd):
                                            player = VideoPlayer()
                                            player.search_videos_tag("#cat")
                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 6
                                            assert "Here are the results for #cat:" in lines[0]
                                            assert "1) Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[1]
                                            assert "2) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                   lines[2]
                                            assert ("Would you like to play any of the above? If yes, "
                                                    "specify the number of the video.") in lines[3]
                                            assert ("If your answer is not a valid number, we will assume "
                                                    "it's a no.") in lines[4]
                                            assert "Playing video: Amazing Cats" in lines[5]

                                        @mock.patch('builtins.input', lambda *args: '5')
                                        def test_search_videos_with_tag_number_out_of_bounds(capfd):
                                            player = VideoPlayer()
                                            player.search_videos_tag("#cat")
                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 5
                                            assert "Here are the results for #cat:" in lines[0]
                                            assert "1) Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[1]
                                            assert "2) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                   lines[2]
                                            assert ("Would you like to play any of the above? If yes, "
                                                    "specify the number of the video.") in lines[3]
                                            assert ("If your answer is not a valid number, we will assume "
                                                    "it's a no.") in lines[4]
                                            assert "Playing video" not in out

                                        def test_search_videos_tag_no_results(capfd):
                                            player = VideoPlayer()
                                            player.search_videos_tag("#blah")
                                            out, err = capfd.readouterr()
                                            lines = out.splitlines()
                                            assert len(lines) == 1
                                            assert "No search results for #blah" in lines[0]
                                            from unittest import mock

                                            from src.video_player import VideoPlayer

                                            def test_flag_video_with_reason(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 1
                                                assert "Successfully flagged video: Amazing Cats (reason: dont_like_cats)" \
                                                       in lines[0]

                                            def test_flag_video_without_reason(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("another_cat_video_id")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 1
                                                assert "Successfully flagged video: Another Cat Video " \
                                                       "(reason: Not supplied)" in lines[0]

                                            def test_flag_video_already_flagged(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 2
                                                assert "Successfully flagged video: Amazing Cats (reason: dont_like_cats)" in \
                                                       lines[0]
                                                assert "Cannot flag video: Video is already flagged" in lines[1]

                                            def test_flag_video_nonexistent(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("video_does_not_exist", "flag_video_reason")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 1
                                                assert "Cannot flag video: Video does not exist" in lines[0]

                                            def test_flag_video_can_no_longer_play(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("amazing_cats_video_id")
                                                player.play_video("amazing_cats_video_id")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 2
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: Not supplied)" in lines[0]
                                                assert "Cannot play video: Video is currently flagged " \
                                                       "(reason: Not supplied)" in lines[1]

                                            def test_flag_videos_play_random(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("funny_dogs_video_id")
                                                player.flag_video("amazing_cats_video_id")
                                                player.flag_video("another_cat_video_id")
                                                player.flag_video("life_at_google_video_id")
                                                player.flag_video("nothing_video_id")
                                                player.play_random_video()
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 6
                                                assert "Successfully flagged video: Funny Dogs " \
                                                       "(reason: Not supplied)" in lines[0]
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: Not supplied)" in lines[1]
                                                assert "Successfully flagged video: Another Cat Video " \
                                                       "(reason: Not supplied)" in lines[2]
                                                assert "Successfully flagged video: Life at Google " \
                                                       "(reason: Not supplied)" in lines[3]
                                                assert "Successfully flagged video: Video about nothing " \
                                                       "(reason: Not supplied)" in lines[4]
                                                assert "No videos available" in lines[5]

                                            def test_flag_video_add_to_playlist(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("amazing_cats_video_id")
                                                player.create_playlist("my_playlist")
                                                player.add_to_playlist("my_playlist", "amazing_cats_video_id")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 3
                                                assert ("Successfully flagged video: Amazing Cats "
                                                        "(reason: Not supplied)") in lines[0]
                                                assert "Successfully created new playlist: my_playlist" in lines[1]
                                                assert ("Cannot add video to my_playlist: Video is currently "
                                                        "flagged (reason: Not supplied)") in lines[2]

                                            def test_flag_video_show_playlist(capfd):
                                                player = VideoPlayer()
                                                player.create_playlist("my_playlist")
                                                player.add_to_playlist("my_playlist", "amazing_cats_video_id")
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.show_playlist("my_playlist")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 5
                                                assert "Successfully created new playlist: my_playlist" in lines[0]
                                                assert "Added video to my_playlist: Amazing Cats" in lines[1]
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: dont_like_cats)" in lines[2]
                                                assert "Showing playlist: my_playlist" in lines[3]
                                                assert ("Amazing Cats (amazing_cats_video_id) [#cat #animal] - FLAGGED "
                                                        "(reason: dont_like_cats)") in lines[4]

                                            def test_flag_video_show_all_videos(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.show_all_videos()
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 7
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: dont_like_cats)" in lines[0]
                                                assert "Here's a list of all available videos:" in lines[1]
                                                assert ("Amazing Cats (amazing_cats_video_id) [#cat #animal] - FLAGGED "
                                                        "(reason: dont_like_cats)") in lines[2]
                                                assert "Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                       lines[3]
                                                assert "Funny Dogs (funny_dogs_video_id) [#dog #animal]" in lines[4]
                                                assert "Life at Google (life_at_google_video_id) [#google #career]" in \
                                                       lines[5]
                                                assert "Video about nothing (nothing_video_id) []" in lines[6]

                                            @mock.patch('builtins.input', lambda *args: 'No')
                                            def test_flag_video_search_videos(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.search_videos("cat")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 5
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: dont_like_cats)" in lines[0]
                                                assert "Here are the results for cat:" in lines[1]
                                                assert "1) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                       lines[2]
                                                assert ("Would you like to play any of the above? If yes, "
                                                        "specify the number of the video.") in lines[3]
                                                assert ("If your answer is not a valid number, we will assume "
                                                        "it's a no.") in lines[4]

                                            @mock.patch('builtins.input', lambda *args: 'No')
                                            def test_flag_video_search_videos_with_tag(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.search_videos_tag("#cat")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 5
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: dont_like_cats)" in lines[0]
                                                assert "Here are the results for #cat:" in lines[1]
                                                assert "1) Another Cat Video (another_cat_video_id) [#cat #animal]" in \
                                                       lines[2]
                                                assert ("Would you like to play any of the above? If yes, "
                                                        "specify the number of the video.") in lines[3]
                                                assert ("If your answer is not a valid number, we will assume "
                                                        "it's a no.") in lines[4]

                                            def test_flag_video_stops_playing_video(capfd):
                                                player = VideoPlayer()
                                                player.play_video("amazing_cats_video_id")
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.show_playing()
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 4
                                                assert "Playing video: Amazing Cats" in lines[0]
                                                assert "Stopping video: Amazing Cats" in lines[1]
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: dont_like_cats)" in lines[2]
                                                assert "No video is currently playing" in lines[3]

                                            def test_flag_video_leaves_video_if_video_is_different(capfd):
                                                player = VideoPlayer()
                                                player.play_video("amazing_cats_video_id")
                                                player.flag_video("another_cat_video_id", "dont_like_cats")
                                                player.show_playing()
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 3
                                                assert "Playing video: Amazing Cats" in lines[0]
                                                assert "Successfully flagged video: Another Cat Video " \
                                                       "(reason: dont_like_cats)" in lines[1]
                                                assert "Currently playing: Amazing Cats (amazing_cats_video_id) " \
                                                       "[#cat #animal]" in lines[2]

                                            def test_flag_video_stops_paused_video(capfd):
                                                player = VideoPlayer()
                                                player.play_video("amazing_cats_video_id")
                                                player.pause_video()
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.show_playing()
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 5
                                                assert "Playing video: Amazing Cats" in lines[0]
                                                assert "Pausing video: Amazing Cats" in lines[1]
                                                assert "Stopping video: Amazing Cats" in lines[2]
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: dont_like_cats)" in lines[3]
                                                assert "No video is currently playing" in lines[4]

                                            def test_allow_video(capfd):
                                                player = VideoPlayer()
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.allow_video("amazing_cats_video_id")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 2
                                                assert "Successfully flagged video: Amazing Cats " \
                                                       "(reason: dont_like_cats)" in lines[0]
                                                assert "Successfully removed flag from video: Amazing Cats" in lines[1]

                                            def test_allow_video_not_flagged(capfd):
                                                player = VideoPlayer()
                                                player.allow_video("amazing_cats_video_id")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 1
                                                assert "Cannot remove flag from video: Video is not flagged" in lines[0]

                                            def test_allow_video_nonexistent(capfd):
                                                player = VideoPlayer()
                                                player.allow_video("video_does_not_exist")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 1
                                                assert "Cannot remove flag from video: Video does not exist" in lines[0]

                                            def test_allow_video_show_playlist(capfd):
                                                player = VideoPlayer()
                                                player.create_playlist("my_playlist")
                                                player.add_to_playlist("my_playlist", "amazing_cats_video_id")
                                                player.flag_video("amazing_cats_video_id", "dont_like_cats")
                                                player.show_playlist("my_playlist")
                                                player.allow_video("amazing_cats_video_id")
                                                player.show_playlist("my_playlist")
                                                out, err = capfd.readouterr()
                                                lines = out.splitlines()
                                                assert len(lines) == 8
                                                assert "Successfully created new playlist: my_playlist" in lines[0]
                                                assert "Added video to my_playlist: Amazing Cats" in lines[1]
                                                assert ("Successfully flagged video: Amazing Cats "
                                                        "(reason: dont_like_cats)") in lines[2]
                                                assert "Showing playlist: my_playlist" in lines[3]
                                                assert ("Amazing Cats (amazing_cats_video_id) [#cat #animal] - FLAGGED "
                                                        "(reason: dont_like_cats)") in lines[4]
                                                assert "Successfully removed flag from video: Amazing Cats" in lines[5]
                                                assert "Showing playlist: my_playlist" in lines[6]
                                                assert "Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[7]
                                                from src.video_library import VideoLibrary

                                                def test_library_has_all_videos():
                                                    library = VideoLibrary()
                                                    assert len(library.get_all_videos()) == 5

                                                def test_parses_tags_correctly():
                                                    library = VideoLibrary()
                                                    video = library.get_video("amazing_cats_video_id")

                                                    assert video is not None
                                                    assert video.title == "Amazing Cats"
                                                    assert video.video_id == "amazing_cats_video_id"
                                                    assert set(video.tags) == {"#cat", "#animal"}

                                                def test_parses_video_correctly_without_tags():
                                                    library = VideoLibrary()
                                                    video = library.get_video("nothing_video_id")

                                                    assert video is not None
                                                    assert video.title == "Video about nothing"
                                                    assert video.video_id == "nothing_video_id"
                                                    assert video.tags == ()