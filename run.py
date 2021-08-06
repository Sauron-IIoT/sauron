from app.repository.capture import fetch_one, save_local, save_remote, get_by_id

capture = fetch_one()
save_local(capture)

print(f'captured picture: {capture["path"]}')
print(f'picture in db: {get_by_id(capture["id"])}')

save_remote(capture)

print(f'capture {capture["id"]} uploaded to s3')