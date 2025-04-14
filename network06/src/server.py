from dnserver import DNSServer

server = DNSServer.from_toml('zones.toml', port=53)
server.start()
assert server.is_running
