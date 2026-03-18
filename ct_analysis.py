"""
ICC Champions Trophy 2025 — Complete Data Analysis
Author: Ahsan Raza
GitHub: ahsanraza6925-prog
Description: Data analysis of ICC Champions Trophy 2025 using Python,
             Pandas, NumPy and Matplotlib.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────
# 1. MATCH DATA
# ─────────────────────────────────────────
matches = pd.DataFrame([
    {'Match': 1,  'Stage': 'Group A',     'Team1': 'New Zealand',  'Score1': '320/9', 'Team2': 'Pakistan',     'Score2': '221',   'Winner': 'New Zealand',  'Margin': '99 runs'},
    {'Match': 2,  'Stage': 'Group A',     'Team1': 'Bangladesh',   'Score1': '228',   'Team2': 'India',        'Score2': '231/3', 'Winner': 'India',        'Margin': '7 wickets'},
    {'Match': 3,  'Stage': 'Group B',     'Team1': 'South Africa', 'Score1': '315/7', 'Team2': 'Afghanistan',  'Score2': '273',   'Winner': 'South Africa', 'Margin': '42 runs'},
    {'Match': 4,  'Stage': 'Group B',     'Team1': 'England',      'Score1': '282/9', 'Team2': 'Australia',    'Score2': '283/5', 'Winner': 'Australia',    'Margin': '5 wickets'},
    {'Match': 5,  'Stage': 'Group A',     'Team1': 'Pakistan',     'Score1': '241',   'Team2': 'India',        'Score2': '245/4', 'Winner': 'India',        'Margin': '6 wickets'},
    {'Match': 6,  'Stage': 'Group A',     'Team1': 'Bangladesh',   'Score1': '236/9', 'Team2': 'New Zealand',  'Score2': '237/4', 'Winner': 'New Zealand',  'Margin': '6 wickets'},
    {'Match': 7,  'Stage': 'Group B',     'Team1': 'Australia',    'Score1': '350/8', 'Team2': 'South Africa', 'Score2': '307',   'Winner': 'Australia',    'Margin': '43 runs'},
    {'Match': 8,  'Stage': 'Group B',     'Team1': 'Afghanistan',  'Score1': '149',   'Team2': 'England',      'Score2': '150/5', 'Winner': 'England',      'Margin': '5 wickets'},
    {'Match': 9,  'Stage': 'Group A',     'Team1': 'Pakistan',     'Score1': '257/6', 'Team2': 'Bangladesh',   'Score2': '208',   'Winner': 'Pakistan',     'Margin': '49 runs'},
    {'Match': 10, 'Stage': 'Group B',     'Team1': 'Afghanistan',  'Score1': '182',   'Team2': 'Australia',    'Score2': '183/2', 'Winner': 'Australia',    'Margin': '8 wickets'},
    {'Match': 11, 'Stage': 'Group B',     'Team1': 'England',      'Score1': '265',   'Team2': 'South Africa', 'Score2': '267/5', 'Winner': 'South Africa', 'Margin': '5 wickets'},
    {'Match': 12, 'Stage': 'Group A',     'Team1': 'India',        'Score1': '249/4', 'Team2': 'New Zealand',  'Score2': '204',   'Winner': 'India',        'Margin': '45 runs'},
    {'Match': 13, 'Stage': 'Semi-Final 1','Team1': 'Australia',    'Score1': '264/7', 'Team2': 'India',        'Score2': '265/4', 'Winner': 'India',        'Margin': '6 wickets'},
    {'Match': 14, 'Stage': 'Semi-Final 2','Team1': 'New Zealand',  'Score1': '362/6', 'Team2': 'South Africa', 'Score2': '312/9', 'Winner': 'New Zealand',  'Margin': '50 runs'},
    {'Match': 15, 'Stage': 'Final',       'Team1': 'New Zealand',  'Score1': '251/7', 'Team2': 'India',        'Score2': '254/6', 'Winner': 'India',        'Margin': '4 wickets'},
])

# ─────────────────────────────────────────
# 2. PLAYER DATA
# ─────────────────────────────────────────
batsmen = pd.DataFrame({
    'Player'  : ['Rachin Ravindra', 'Rohit Sharma', 'Shubman Gill', 'Daryl Mitchell',
                 'Virat Kohli', 'Travis Head', 'Babar Azam', 'Shreyas Iyer'],
    'Country' : ['New Zealand', 'India', 'India', 'New Zealand',
                 'India', 'Australia', 'Pakistan', 'India'],
    'Runs'    : [343, 301, 288, 268, 241, 217, 192, 185],
    'Matches' : [5, 5, 5, 5, 5, 4, 3, 5],
    'Highest' : [111, 76, 101, 134, 100, 84, 91, 89]
})
batsmen['Average'] = (batsmen['Runs'] / batsmen['Matches']).round(1)

bowlers = pd.DataFrame({
    'Player'  : ['Matt Henry', 'Varun Chakravarthy', 'Mohammed Shami', 'Trent Boult',
                 'Kuldeep Yadav', 'Mitchell Santner', 'Adam Zampa', 'Shaheen Afridi'],
    'Country' : ['New Zealand', 'India', 'India', 'New Zealand',
                 'India', 'New Zealand', 'Australia', 'Pakistan'],
    'Wickets' : [10, 9, 8, 7, 7, 6, 6, 5],
    'Matches' : [4, 3, 5, 5, 5, 5, 4, 3],
    'Best'    : ['4/28', '3/25', '3/36', '3/42', '3/32', '2/19', '3/44', '3/38']
})

# ─────────────────────────────────────────
# 3. KEY INSIGHTS
# ─────────────────────────────────────────
print("=" * 50)
print("ICC CHAMPIONS TROPHY 2025 — KEY INSIGHTS")
print("=" * 50)

win_counts = matches['Winner'].value_counts()
print("\nTeam Wins:")
for team, wins in win_counts.items():
    print(f"  {team:<20}: {wins} wins")

print(f"\nTop Run Scorer   : {batsmen.iloc[0]['Player']} — {batsmen.iloc[0]['Runs']} runs")
print(f"Top Wicket Taker : {bowlers.iloc[0]['Player']} — {bowlers.iloc[0]['Wickets']} wickets")
print(f"Champion         : India (Unbeaten — 5/5)")
print(f"Player of Tournament: Rachin Ravindra (NZ)")

# ─────────────────────────────────────────
# 4. VISUALIZATIONS
# ─────────────────────────────────────────
team_colors = {
    'India': '#1a75ff', 'New Zealand': '#2d2d2d', 'Australia': '#FFD700',
    'South Africa': '#006400', 'Pakistan': '#01411C', 'England': '#CF142B',
    'Bangladesh': '#006A4E', 'Afghanistan': '#0032A0'
}

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('ICC Champions Trophy 2025 — Data Analysis 🏆', fontsize=16, fontweight='bold')

# Plot 1: Team Wins
win_df = win_counts.reset_index()
win_df.columns = ['Team', 'Wins']
colors1 = [team_colors.get(t, 'gray') for t in win_df['Team']]
bars = axes[0,0].barh(win_df['Team'], win_df['Wins'], color=colors1, edgecolor='white')
for bar, val in zip(bars, win_df['Wins']):
    axes[0,0].text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
                   str(val), va='center', fontweight='bold')
axes[0,0].set_title('Total Wins per Team', fontweight='bold')
axes[0,0].set_xlabel('Wins')
axes[0,0].invert_yaxis()

# Plot 2: Top Run Scorers
bat_colors = [team_colors.get(c, 'gray') for c in batsmen['Country']]
bars2 = axes[0,1].bar(batsmen['Player'], batsmen['Runs'], color=bat_colors, edgecolor='white', width=0.6)
for bar, val in zip(bars2, batsmen['Runs']):
    axes[0,1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                   str(val), ha='center', fontsize=8, fontweight='bold')
axes[0,1].set_title('Top Run Scorers', fontweight='bold')
axes[0,1].set_ylabel('Runs')
axes[0,1].set_xticklabels([p.split()[-1] for p in batsmen['Player']], rotation=45, ha='right')

# Plot 3: Top Wicket Takers
bowl_colors = [team_colors.get(c, 'gray') for c in bowlers['Country']]
bars3 = axes[1,0].bar(bowlers['Player'], bowlers['Wickets'], color=bowl_colors, edgecolor='white', width=0.6)
for bar, val in zip(bars3, bowlers['Wickets']):
    axes[1,0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                   str(val), ha='center', fontsize=9, fontweight='bold')
axes[1,0].set_title('Top Wicket Takers', fontweight='bold')
axes[1,0].set_ylabel('Wickets')
axes[1,0].set_xticklabels([p.split()[-1] for p in bowlers['Player']], rotation=45, ha='right')

# Plot 4: Win Share Pie
pie_colors = [team_colors.get(t, 'gray') for t in win_df['Team']]
axes[1,1].pie(win_df['Wins'], labels=win_df['Team'], colors=pie_colors,
              autopct='%1.0f%%', startangle=90, textprops={'fontsize': 9})
axes[1,1].set_title('Win Share %', fontweight='bold')

plt.tight_layout()
plt.savefig('champions_trophy_2025_analysis.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nVisualization saved!")
print("\nAnalysis Complete! 🏆")
