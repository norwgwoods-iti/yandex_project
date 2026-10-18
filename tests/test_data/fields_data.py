
FIELD_CONTENT_FILE_METADATA = {
    "path": str,
    "type": str,
    "created": str,
    "modified": str,
    "size": int,
    "mime_type": str,
    "md5": str,
    "sha256": str,
    "preview": str,
    "media_type": str,
    "sizes": list,
    "resource_id": str,
    "revision": int,
    'comment_ids': {
        "public_resource": str,
        "private_resource": str
    },
    "exif": dict,
    "antivirus_status": str,
    "file": str,
}


FIELD_DIR_METADATA = {
    "path": str,
    "type": str,
    "name": str,
    "created":str,
    "modified": str,
    "_embedded": {
        "path": str,
        "limit": int,
        "offset": int,
        "sort": str,
        "total": int,
        "items": list
    },
    "resource_id": str,
    "revision": int,
    "comment_ids": {
        "public_resource": str,
        "private_resource": str
    },
    "exif": dict,
}


FIELD_CONTENT_UPLOAD_DIR_OR_FILE = {
    'method': str,
    'href': str,
    'templated': bool
}
