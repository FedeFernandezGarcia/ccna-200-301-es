import ipaddress as ip

bloque = ip.ip_network("172.16.0.0/22")
pedidos = [("Sede central", 500), ("Sucursal A", 200), ("Sucursal B", 100),
           ("Sucursal C", 50), ("Enlace WAN 1", 2), ("Enlace WAN 2", 2)]

cur = int(bloque.network_address)
print("Bloque:", bloque, "va de", bloque.network_address, "a", bloque.broadcast_address,
      "total", bloque.num_addresses)
print()

for nombre, need in pedidos:
    bits = 1
    while (2 ** bits - 2) < need:
        bits += 1
    pref = 32 - bits
    size = 2 ** bits
    if cur % size:
        cur += size - (cur % size)
    n = ip.ip_network((cur, pref))
    fh = n.network_address + 1 if pref < 31 else n.network_address
    lh = n.broadcast_address - 1 if pref < 31 else n.broadcast_address
    print(nombre.ljust(14), "pide", str(need).rjust(3), "prefijo", pref,
          "red", str(n.network_address).ljust(14),
          "rango", str(fh).ljust(14), "a", str(lh).ljust(14),
          "bcast", str(n.broadcast_address).ljust(14), "da", 2 ** bits - 2)
    cur += size

print()
print("Siguiente libre:", ip.ip_address(cur), "fin del bloque:", bloque.broadcast_address)
print("Usadas:", cur - int(bloque.network_address), "de", bloque.num_addresses)
