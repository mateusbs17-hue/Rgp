TA = """
    -- TODO: SELECT ... FROM inventario JOIN personagens ... JOIN itens ...
"""


def incluir(conn, personagem_id, item_id, quantidade):
    """Coloca um item no inventário de um personagem e devolve o id gerado."""
    # TODO
    raise NotImplementedError


def buscar_por_id(conn, id):
    """Devolve UMA linha, ou None."""
    # TODO
    raise NotImplementedError


def buscar_por_nome(conn, nome_personagem):
    """Devolve uma LISTA com os itens dos personagens cujo nome contém o texto."""
    # TODO
    raise NotImplementedError


def listar(conn):
    """Devolve uma LISTA com todo o inventário."""
    # TODO
    raise NotImplementedError
