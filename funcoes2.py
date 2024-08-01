def loginUsuario(perfil):
    if perfil == 'admin':
        print('Bem-vindo, Administrador.')
    else:
        print('Bem-vindo usuário.')
    return

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('etc')
