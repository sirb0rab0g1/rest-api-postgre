import os


def upload_image_path(instance, filename):
    return os.path.join('images', instance.__class__.__name__.lower(), str(instance.id), filename)
