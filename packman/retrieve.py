import utils
import sys
import logger
import os
import codes
import requests

lgr = logger.init()


def download_file(url, destination):
    """downloads a file to a destination
    """
    destination = destination if destination else url.split('/')[-1]
    r = requests.get(url, stream=True)
    if not r.status_code == 200:
        lgr.error('Could not download file: {0}'.format(url))
        return False
    with open(destination, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return True


class Handler(utils.Handler):
    def downloads(self, urls, dir=False):
        """wgets a list of urls to a destination directory

        :param list urls: a list of urls to download
        :param string dir: download to dir...
        """
        for source_url in urls:
            url_ext = os.path.splitext(source_url)[1]
            # if the source file is an rpm or deb, we want to download
            # it to the archives folder. yes, it's a dreadful solution...
            if url_ext in ('.rpm', '.deb'):
                lgr.debug('The file is a {0} file. we\'ll download it '
                          'to the archives folder'.format(url_ext))
                self.download(source_url, dir=os.path.join(dir, 'archives'))
            else:
                self.download(source_url, dir=dir)

    def download(self, url, dir=False, file=False):
        u = utils.Handler()
        if (file and dir) or (not file and not dir):
            lgr.warning('Please specify either a directory'
                        ' or file to download to.')
            sys.exit(codes.mapping['must_specify_file_or_dir'])
        destination = dir or file
        if u.is_dir(destination):
            destination = os.path.join(dir, url.split('/')[-1])
        lgr.debug('Downloading {0} to {1}'.format(url, destination))
        outcome = download_file(url, destination)
        if not outcome:
            sys.exit(codes.mapping['failed_to_download_file'])
