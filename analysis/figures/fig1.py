"""Figure 1: annual % change in RN employment vs. real median RN wage, OEWS 2015-2019."""
import os, csv
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"Liberation Serif","font.size":11})
here=os.path.dirname(os.path.abspath(__file__)); data=os.path.join(here,"..","..","data")
oews={int(r["year"]):r for r in csv.DictReader(open(os.path.join(data,"oews_rn_2015_2019.csv")))}
cpi={int(r["year"]):float(r["cpi_u_annual_avg"]) for r in csv.DictReader(open(os.path.join(data,"cpi_u_annual.csv")))}
yrs=range(2015,2020)
emp={y:float(oews[y]["rn_employment"]) for y in yrs}
real={y:float(oews[y]["median_annual_wage_nominal"])/cpi[y] for y in yrs}
pts=[(y,(real[y]/real[y-1]-1)*100,(emp[y]/emp[y-1]-1)*100) for y in range(2016,2020)]
cum_e=(emp[2019]/emp[2015]-1)*100; cum_w=(real[2019]/real[2015]-1)*100
INK="#0b0b0b"; INK2="#52514e"; GRID="#e4e3df"; B="#2a78d6"
fig,ax=plt.subplots(figsize=(6.5,4.2),dpi=300)
ax.fill_between([0,4.5],[0,4.5],[0,0],color="#f3f2ef",zorder=0)
ax.plot([0,4.5],[0,4.5],color=INK2,lw=1,ls=(0,(4,3)),zorder=1)
ax.text(2.2,0.9,"Dashed line: ratio = 1.0\nShaded area (below it): consistent\nwith inelastic supply",color=INK2,fontsize=9,va="top")
for y,x,e in pts:
    ax.plot(x,e,"o",ms=8,color=B,mec="white",mew=1.5,zorder=3)
    ax.annotate(f"{y}  (ratio {e/x:.1f})",(x,e),xytext=(9,-3),textcoords="offset points",fontsize=9,color=INK)
ax.set_xlim(0,4.5); ax.set_ylim(0,4.5); ax.set_aspect("equal")
ax.set_xlabel("Annual % change in real median RN wage (2019 dollars)",color=INK)
ax.set_ylabel("Annual % change in RN employment",color=INK)
for sp in("top","right"): ax.spines[sp].set_visible(False)
for sp in("left","bottom"): ax.spines[sp].set_color(INK2)
ax.tick_params(colors=INK2); ax.grid(color=GRID,lw=0.8); ax.set_axisbelow(True)
fig.savefig(os.path.join(here,"figure1_employment_wage_1.png"),bbox_inches="tight",facecolor="white")
print([(y,round(x,2),round(e,2)) for y,x,e in pts], round(cum_e,2), round(cum_w,2), round(cum_e/cum_w,1))
