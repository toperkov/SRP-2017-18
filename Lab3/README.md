# Upute za korištenje Lab. vježbe 3

* pinganje računala:

```bash
for i in $(seq 1 20); do echo "Testing 171.17.0.$i"; ping -c1 -t 20 -w 172.17.0.$i| grep "64 bytes" ; done
```

