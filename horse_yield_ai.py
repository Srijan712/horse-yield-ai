import json
import yaml
from datetime import datetime

# Load configuration
def load_config(config_file='config.yaml'):
    """Load configuration from YAML file"""
    try:
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Config file {config_file} not found")
        return {}

# Core Calculation Functions
def calculate_monthly_income(events_per_month, price_per_event):
    """Calculate monthly income from events"""
    return events_per_month * price_per_event

def calculate_monthly_costs(feed_cost, maintenance_cost, transport_cost):
    """Calculate total monthly costs"""
    return feed_cost + maintenance_cost + transport_cost

def calculate_monthly_profit(monthly_income, monthly_costs):
    """Calculate monthly profit"""
    return monthly_income - monthly_costs

def calculate_working_years(age, health_score, config):
    """Calculate remaining working years based on age and health"""
    if age < 3:
        working_years = 0
    elif age <= 10:
        if health_score >= 8:
            working_years = 10 - age
        else:
            working_years = max(5, 10 - age)
    elif age <= 15:
        working_years = 15 - age
    else:
        working_years = max(1, 20 - age)
    
    return max(0, working_years)

def calculate_lifetime_earnings(monthly_profit, working_years):
    """Calculate total lifetime earnings"""
    months = working_years * 12
    return monthly_profit * months

def calculate_roi(total_profit, total_investment):
    """Calculate Return on Investment"""
    if total_investment == 0:
        return 0
    return (total_profit / total_investment) * 100

def assess_risk(age, health_score, demand_per_month, monthly_profit):
    """Assess risk level based on various factors"""
    risk_score = 0
    
    # Health risk
    if health_score < 5:
        risk_score += 30
    elif health_score < 7:
        risk_score += 15
    
    # Age risk
    if age < 3 or age > 18:
        risk_score += 25
    
    # Demand risk
    if demand_per_month < 5:
        risk_score += 20
    
    # Profit risk
    if monthly_profit < 10000:
        risk_score += 20
    
    # Determine risk level
    if risk_score >= 60:
        return "High"
    elif risk_score >= 30:
        return "Medium"
    else:
        return "Low"

def analyze_horse(horse_data, config):
    """Comprehensive horse yield analysis"""
    
    # Extract data
    age = horse_data.get('age')
    health_score = horse_data.get('health_score')
    events_per_month = horse_data.get('events_per_month')
    price_per_event = horse_data.get('price_per_event')
    feed_cost = horse_data.get('feed_cost')
    maintenance_cost = horse_data.get('maintenance_cost')
    transport_cost = horse_data.get('transport_cost')
    demand_per_month = horse_data.get('demand_per_month')
    total_investment = horse_data.get('total_investment', 0)
    
    # Calculations
    monthly_income = calculate_monthly_income(events_per_month, price_per_event)
    monthly_costs = calculate_monthly_costs(feed_cost, maintenance_cost, transport_cost)
    monthly_profit = calculate_monthly_profit(monthly_income, monthly_costs)
    working_years = calculate_working_years(age, health_score, config)
    lifetime_earnings = calculate_lifetime_earnings(monthly_profit, working_years)
    roi = calculate_roi(lifetime_earnings, total_investment) if total_investment > 0 else 0
    risk_level = assess_risk(age, health_score, demand_per_month, monthly_profit)
    
    # Build result
    result = {
        'horse_name': horse_data.get('name', 'Unknown'),
        'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'input_parameters': horse_data,
        'output_results': {
            'monthly_income': monthly_income,
            'monthly_costs': monthly_costs,
            'monthly_profit': monthly_profit,
            'working_years': working_years,
            'lifetime_earnings': lifetime_earnings,
            'roi_percentage': round(roi, 2),
            'risk_level': risk_level
        }
    }
    
    return result

def print_analysis(analysis):
    """Pretty print analysis results"""
    print("\n" + "="*60)
    print(f"HORSE YIELD AI - ANALYSIS REPORT")
    print("="*60)
    print(f"Horse: {analysis['horse_name']}")
    print(f"Date: {analysis['analysis_date']}")
    print("-"*60)
    
    results = analysis['output_results']
    
    print("\n📊 FINANCIAL METRICS:")
    print(f"  Monthly Income:        ₹{results['monthly_income']:,.2f}")
    print(f"  Monthly Costs:         ₹{results['monthly_costs']:,.2f}")
    print(f"  Monthly Profit:        ₹{results['monthly_profit']:,.2f}")
    
    print("\n📈 LIFETIME PROJECTIONS:")
    print(f"  Working Years:         {results['working_years']} years")
    print(f"  Lifetime Earnings:     ₹{results['lifetime_earnings']:,.2f}")
    print(f"  ROI:                   {results['roi_percentage']}%")
    
    print("\n⚠️  RISK ASSESSMENT:")
    print(f"  Risk Level:            {results['risk_level']}")
    
    print("="*60 + "\n")

# Example usage
if __name__ == "__main__":
    # Load configuration
    config = load_config('config.yaml')
    
    # Example horse data
    horse = {
        'name': 'Thunder',
        'age': 5,
        'breed': 'Thoroughbred',
        'health_score': 9,
        'training_level': 'Advanced',
        'events_per_month': 10,
        'price_per_event': 8000,
        'feed_cost': 10000,
        'maintenance_cost': 15000,
        'transport_cost': 5000,
        'demand_per_month': 12,
        'total_investment': 500000
    }
    
    # Run analysis
    analysis = analyze_horse(horse, config)
    
    # Display results
    print_analysis(analysis)
    
    # Save results to JSON
    with open('analysis_output.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    print("✅ Analysis saved to analysis_output.json")
