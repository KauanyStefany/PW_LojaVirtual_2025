from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    Nome: str
    CPF: str
    Email: str
    Telefone: str
    Senha: str
