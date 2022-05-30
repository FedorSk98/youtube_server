from pytube import YouTube


class YoutubeRequest:
    """Получение информации с YouTube через pytube"""

    def request_data(self, base_url) -> dict:
        """Получаем информацию о видео по ссылке
        :param base_url:  ссылка на видео"""

        you_tube = YouTube(base_url)
        data_video = {
            'video_id': you_tube.video_id,
            'title': you_tube.title,
            'author': you_tube.author,
            'photo': you_tube.thumbnail_url,
            'audio_url': you_tube.streams.get_audio_only().url,
        }

        return data_video

