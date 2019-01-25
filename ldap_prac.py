import ldap

conn=ldap.initialize("ldap://localhost")
print(conn, type(conn))
print(conn.simple_bind_s())

