from dataclasses import dataclass

@dataclass
class FinancialRecord:
    description: str
    amount: float
    type: str  # 'income' or 'expense'
