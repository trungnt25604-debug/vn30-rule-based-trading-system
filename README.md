# VN30 Rule-Based Trading Decision Support System

## Overview
This project implements a rule-based decision support system for VN30 stocks
using technical indicators such as MA, RSI, MACD and slope of MA.

The system does not automatically execute trades, but provides Hold/Sell
recommendations to support investor decision-making.

## Main Components
- Data loader for historical stock prices
- Technical indicator calculation
- Rule-based recommendation engine
- Portfolio monitoring and alert system
- Backtesting module

## Data
Historical EOD price data (2023–2025) collected from VNStock.

## How to Run
```bash
python main.py
python backtest.py

Author

Nguyen Thanh Trung
