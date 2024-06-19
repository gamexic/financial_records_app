from dataclasses import dataclass

@dataclass
class FinancialRecord:
    id: int
    description: str
    amount: float
    type: str  # 'income' or 'expense'
