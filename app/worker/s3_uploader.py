from app.repository.capture import get_all, save_remote, delete_local

captures = get_all()

for capture in captures:
    print(f'started uploading capture to s3: {capture}')
    print(f'{capture["id"]}')
    save_remote(capture)
    print(f'capture {capture["id"]} uploaded to s3')

    print(f'deleting capture from local storage: {capture["id"]}')
    delete_local(capture)
    print(f'capture deleted from local storage: {capture["id"]}')