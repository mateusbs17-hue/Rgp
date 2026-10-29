# Parte comum das consultas. Complete o segundo JOIN (classes).
CONSULTA = """
    SELECT personagens.id, personagens.nome, personagens.nivel,
           jogadores.apelido, classes.nome
    FROM personagens
    JOIN jogadores ON jogadores.id = personagens.jogador_id
"""
# TODO: acrescente acima a linha
#       JOIN classes ON classes.id = personagens.classe_id


def incluir(conn, nome, nivel, jogador_id, classe_id):
    """Insere um personagem e devolve o id gerado."""
    # TODO
    raise NotImplementedError


def buscar_por_id(conn, id):
    """Devolve UMA linha, ou None.
    Dica: conn.execute(CONSULTA + " WHERE personagens.id = ?", (id,))"""
    # TODO
    raise NotImplementedError


def buscar_por_nome(conn, nome):
    """Devolve uma LISTA com os personagens cujo nome contém o texto."""
    # TODO: cuidado, aqui é personagens.nome (classes também tem coluna nome)
    raise NotImplementedError


def listar(conn):
    """Devolve uma LISTA com todos os personagens."""
    # TODO
    raise NotImplementedError
