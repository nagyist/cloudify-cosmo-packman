import utils
import exceptions
import logger

lgr = logger.init()


class Handler(utils.Handler):
    def downloads(self, urls, dir=False, sudo=True):
        """wgets a list of urls to a destination directory

        :param list urls: a list of urls to download
        :param string dir: download to dir...
        """
        for url in urls:
            self.download(url, dir, sudo)

    def download(self, url, dir, sudo):
        options = '--timeout=30'
        # workaround for archives folder
        if (file and dir) or (not file and not dir):
            lgr.warning('please specify either a directory'
                        ' or file to download to.')
            raise exceptions.PackagerError('please specify either a directory'
                                           ' or file to download to.')
        lgr.debug('downloading {0} to {1}'.format(url, file or dir))
        utils.do('wget {0} {1} -O {2}'.format(
            url, options, file), sudo=sudo) \
            if file else utils.do('wget {0} {1} -P {2}'.format(
                url, options, dir), sudo=sudo)
