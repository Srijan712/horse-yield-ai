# Horse Yield AI

Predictive analytics for horse lifetime economic value

## 🎯 Overview
Horse Yield AI estimates the total economic value a horse can generate over its lifetime based on business usage, costs, and market factors.

## 📊 How It Works

### Inputs
**A. Horse Details**
- Age
- Breed
- Weight
- Health Score (1–10)
- Training Level

**B. Business Usage**
- Usage Type (Wedding / Tourism / Mixed)
- Events per month
- Price per event

**C. Cost Factors**
- Feed cost per month
- Maintenance cost
- Transport cost

**D. Market Factors**
- Demand per month
- Seasonal variation (optional)

### Core Calculations

**Monthly Income**
```
Monthly Income = Events per month × Price per event
```

**Monthly Profit**
```
Monthly Profit = Monthly Income – Total Monthly Costs
```

**Active Working Years**
- Peak: 3–10 years
- Medium: 10–15 years
- Decline: 15+ years

**Lifetime Earnings**
```
Lifetime Earnings = Monthly Profit × Remaining Months
```

**ROI**
```
ROI = (Total Profit / Total Investment) × 100
```

### Outputs
- Lifetime Earnings
- Monthly Profit
- Remaining Working Years
- ROI Percentage
- Risk Level (Low / Medium / High)
- Best Usage Recommendation

## 📥 Example

**Inputs:**
- Age: 5 years
- Events/month: 10
- Price/event: ₹8000
- Costs/month: ₹30000

**Output:**
- Monthly Income: ₹80000
- Monthly Profit: ₹50000
- Lifetime Earnings (10 years): ₹60,00,000

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Srijan712/horse-yield-ai.git
cd horse-yield-ai

# Install dependencies
pip install -r requirements.txt

# Run the application
python horse_yield_ai.py
```

## 🔮 Future Scope
- Extend to goats, cows, camels
- Mobile app integration
- Machine learning price prediction
- Marketplace integration

## 📄 License
MIT License - See LICENSE file for details