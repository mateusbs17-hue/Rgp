def incluir(conn, nome, apelido):
    """Insere um jogador e devolve o id gerado."""
    # TODO: INSERT INTO jogadores (nome, apelido) VALUES (?, ?)
    raise NotImplementedError


def buscar_por_id(conn, id):
    """Devolve UMA linha (id, nome, apelido), ou None."""
    # TODO
    raise NotImplementedError


def buscar_por_nome(conn, nome):
    """Devolve uma LISTA com os jogadores cujo nome contém o texto."""
    # TODO: use LIKE e "%" + nome + "%"
    raise NotImplementedError


def listar(conn):
    """Devolve uma LISTA com todos os jogadores (id, nome, apelido)."""
    # TODO
    raise NotImplementedError
