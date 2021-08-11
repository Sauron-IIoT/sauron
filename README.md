### Dependencies
- Docker & Docker Compose
- AWS CLI

### How to run

⚠️ Important: Change `camera_address` host in `settings.toml` to your iot-camera webserver host

Configure AWS credentials:
```
make config
```

Run all services:
```
make run
```

And to stop:
```
make stop
```