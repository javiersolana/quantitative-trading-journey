# 📊 Complete Trading Metrics Glossary

*A comprehensive guide to understanding quantitative trading performance metrics*

## 💰 Basic Performance Metrics

### **Equity**
**Definition:** Total value of your trading account at any given moment.  
**Formula:** Cash + Holdings Value  
**Example:** You start with €100,000 cash. You buy €80,000 in stocks. Your equity = €20,000 cash + €80,000 stocks = €100,000 total  
**Why Important:** Shows your account's real-time worth. If equity grows consistently, your strategy is working.

### **Fees**
**Definition:** Transaction costs paid to brokers for executing trades.  
**Components:** Commission fees, spread costs, slippage  
**Example:** Buy 100 shares at €0.01 per share = €1 fee. In backtesting, QuantConnect simulates realistic fees  
**Reality Check:** High-frequency strategies can be killed by fees. Always include realistic fee assumptions.

### **Holdings**
**Definition:** Current market value of all positions you own.  
**Example:** Own 10 Apple shares at €150 each = €1,500 holdings. Own 5 Tesla shares at €200 each = €1,000 holdings. Total holdings = €2,500  
**Dynamic:** Changes every second as stock prices move. Holdings ≠ what you paid (that's cost basis).

### **Net Profit**
**Definition:** Total money gained or lost since strategy started.  
**Formula:** Current Equity - Initial Capital  
**Example:** Started with €100,000, now have €156,173 → Net Profit = €56,173 (56.17%)  
**Key Insight:** This is your actual money made. Everything else is just analysis of HOW you made it.

### **Return**
**Definition:** Percentage gain/loss from initial investment.  
**Formula:** (Final Value - Initial Value) / Initial Value × 100  
**Example:** €100,000 → €156,173 = (156,173 - 100,000) / 100,000 × 100 = 56.17% return  
**Time Context:** Can be daily, monthly, annual, or total return depending on timeframe.

### **Unrealized**
**Definition:** Paper profit/loss on positions you still own (haven't sold yet).  
**Example:** Bought Tesla at €200, now worth €250. Unrealized gain = €50 per share. Only becomes "realized" when you sell  
**Psychology:** Unrealized gains can disappear! Don't count them as real money until you sell.

### **Volume**
**Definition:** Total dollar amount traded during the period.  
**Example:** Bought €50,000 SPY, sold €30,000 bonds, bought €20,000 gold = €100,000 total volume  
**Importance:** High volume = more transaction costs. Low volume strategies are often more profitable.

## 📈 Risk-Adjusted Performance Metrics

### **Sharpe Ratio**
**Definition:** Return per unit of risk taken. The most important metric for professional traders.  
**Formula:** (Portfolio Return - Risk-free Rate) / Portfolio Standard Deviation  
**Scale:**
- < 0: Poor (losing money vs safe investments)
- 0 - 1: Decent (acceptable risk-adjusted returns)  
- 1 - 2: Good (solid professional level)
- \> 2: Excellent (top-tier performance)

**Example:** Your strategy returns 12% annually with 18% volatility. Risk-free rate is 3%.  
Sharpe = (12% - 3%) / 18% = 0.5 (decent but room for improvement)

**Real World:** Warren Buffett's long-term Sharpe ≈ 0.8. Renaissance Technologies (best hedge fund) ≈ 2.0+

### **Compounding Annual Return (CAR)**
**Definition:** The constant annual return rate that would produce the same total return.  
**Why Important:** Accounts for compounding effect - returns earning returns.  
**Formula:** (Final Value / Initial Value)^(1/years) - 1  
**Example:** €100k → €156k in 4 years  
CAR = (156,173/100,000)^(1/4) - 1 = 11.8% per year  
**Reality:** 11.8% annually beats 90% of professional fund managers.

### **Drawdown**
**Definition:** Peak-to-trough decline in equity value. Measures worst losses.  
**Types:**
- **Current Drawdown:** How far down you are from recent peak
- **Maximum Drawdown:** Worst loss period in entire backtest

**Example:** Account goes €100k → €120k → €80k → €110k  
Max Drawdown = (120k - 80k) / 120k = 33.3%

**Psychology:** 33% drawdown means watching €30,000 disappear. Can you emotionally handle that?

### **Sortino Ratio**
**Definition:** Like Sharpe Ratio, but only penalizes downside volatility (ignores upside volatility).  
**Why Better:** Upside volatility is good (big gains). Only downside volatility hurts.  
**Formula:** (Return - Risk-free Rate) / Downside Standard Deviation  
**Example:** Strategy with wild upside swings (+50% months) but limited downside (-5% max) has better Sortino than Sharpe  
**Interpretation:** Higher Sortino = better downside protection.

## 🎯 Benchmark Comparison Metrics

### **Alpha**
**Definition:** Return above/below benchmark performance. The holy grail of active management.  
**Formula:** Portfolio Return - (Beta × Benchmark Return)  
**Example:** SPY returns 10%, your strategy returns 12%, your beta is 1.0  
Alpha = 12% - (1.0 × 10%) = +2% (you beat market by 2%)

**Reality Check:**
- Positive Alpha = You're adding value beyond market exposure
- Negative Alpha = You'd be better off buying index funds
- Most professionals fail to generate positive alpha consistently

### **Beta**
**Definition:** How much your strategy moves relative to the market.  
**Scale:**
- Beta = 1.0: Moves exactly with market (SPY buy & hold)
- Beta > 1.0: More volatile than market (amplifies market moves)  
- Beta < 1.0: Less volatile than market (defensive)
- Beta = 0: No correlation with market (market neutral strategies)

**Example:** Market goes up 10%, your strategy goes up 15% → Beta ≈ 1.5  
**Risk Implication:** High beta = higher returns in bull markets, worse losses in bear markets.

### **Information Ratio**
**Definition:** Alpha per unit of tracking error. Measures consistency of outperformance.  
**Formula:** Alpha / Tracking Error  
**Example:** You beat benchmark by 2% annually (alpha) but with 8% tracking error  
Information Ratio = 2% / 8% = 0.25  
**Scale:** > 0.5 is considered good, > 1.0 is excellent  
**Importance:** Shows if outperformance is skill or luck.

### **Tracking Error**
**Definition:** Standard deviation of difference between your returns and benchmark returns.  
**Example:** Some months you beat SPY by 3%, others you lag by 2%. The volatility of these differences is tracking error  
**Low Tracking Error:** Close to benchmark (index-like)  
**High Tracking Error:** Very different from benchmark (concentrated bets)  
**Sweet Spot:** Enough tracking error to generate alpha, not so much that you're gambling.

### **Treynor Ratio**
**Definition:** Return per unit of systematic (market) risk.  
**Formula:** (Portfolio Return - Risk-free Rate) / Beta  
**vs Sharpe:** Treynor uses beta (market risk), Sharpe uses total volatility  
**When Useful:** Comparing strategies with different market exposures  
**Example:** Strategy A: 15% return, beta 1.5. Strategy B: 12% return, beta 1.0  
Risk-free rate 3%. Treynor A = (15%-3%)/1.5 = 8%. Treynor B = (12%-3%)/1.0 = 9%  
Strategy B is better at generating return per unit of market risk.

## 📊 Statistical Risk Metrics

### **Annual Standard Deviation**
**Definition:** Measure of how much returns vary from average return (volatility).  
**Formula:** Standard deviation of returns, annualized  
**Example:** Monthly returns of +3%, -1%, +5%, -2%, +4%  
Standard deviation ≈ 3%, annualized ≈ 10.4%  
**Scale:** SPY ≈ 16%, Bonds ≈ 5%, Individual stocks ≈ 20-40%  
**Importance:** Higher volatility = bumpier ride, higher potential returns, higher risk.

### **Annual Variance**
**Definition:** Square of standard deviation. Statistical measure of dispersion.  
**Formula:** (Standard Deviation)²  
**Example:** 18% standard deviation → 0.18² = 0.0324 variance  
**Usage:** More sensitive to extreme outliers than standard deviation  
**Practical:** Most people focus on standard deviation since it's in same units as returns.

### **PSR (Probabilistic Sharpe Ratio)**
**Definition:** Probability that observed Sharpe ratio reflects true skill vs luck.  
**Range:** 0% to 100%  
**Example:** PSR of 95% means 95% confidence that your Sharpe ratio is genuinely positive  
**Your Result:** 11.981% suggests about 12% probability - relatively low confidence  
**Reality Check:** Short backtests have low PSR. Need longer track records for confidence.

## 🔄 Portfolio Management Metrics

### **Estimated Strategy Capacity**
**Definition:** Maximum capital that can be deployed before strategy performance degrades.  
**Factors:** Market impact, liquidity constraints, slippage  
**Example:** Strategy works with €1M but fails with €100M due to moving markets when trading  
**Your Case:** €58M capacity for SPY buy & hold (very high - SPY is liquid)  
**Reality:** Most complex strategies have much lower capacity.

### **Portfolio Turnover**
**Definition:** How frequently you trade relative to portfolio size.  
**Formula:** (Purchases + Sales) / Average Portfolio Value  
**Example:** €100k portfolio, buy €50k, sell €30k in a year  
Turnover = (50k + 30k) / 100k = 80%  
**Your Strategy:** 0.07% turnover (extremely low - buy & hold trades once)  
**Impact:** High turnover = higher fees, more taxes, more complexity.

### **Drawdown Recovery**
**Definition:** Time taken to recover from maximum drawdown to new high.  
**Example:** Peak at €120k, drop to €80k (33% drawdown), takes 18 months to reach €121k  
Drawdown Recovery = 18 months  
**Your Case:** 708 days (almost 2 years) - the COVID recovery period  
**Psychology:** Long recovery periods test investor patience. Many quit during recovery phase.

---

## 🎯 How to Use These Metrics

### **For Strategy Development:**
1. **Start with Sharpe Ratio** - Is risk-adjusted return decent?
2. **Check Max Drawdown** - Can you emotionally handle worst loss?
3. **Analyze Alpha** - Are you beating the market?
4. **Review Turnover** - Are you overtrading?

### **For Strategy Comparison:**
- **Same risk level:** Compare by Sharpe ratio
- **Different risk levels:** Use Sortino ratio  
- **vs Market benchmark:** Focus on Alpha and Information ratio
- **Real-world implementation:** Consider capacity and turnover

### **Red Flags:**
- Sharpe > 3.0 (probably overfit/unrealistic)
- Drawdown > 50% (psychological torture)  
- Very low PSR (likely random luck)
- Extreme turnover (transaction cost killer)

### **Green Flags:**
- Consistent positive alpha across different periods
- Sharpe > 1.0 with reasonable drawdown  
- Short drawdown recovery periods
- Strategy works across different market conditions

---

*Remember: Past performance doesn't guarantee future results. These metrics help you understand what happened, not what will happen. Use them to build intuition and improve your strategies systematically.*

**Pro Tip:** Focus on 3-5 key metrics rather than trying to optimize everything. Sharpe ratio, max drawdown, and alpha are usually sufficient for most decisions.
