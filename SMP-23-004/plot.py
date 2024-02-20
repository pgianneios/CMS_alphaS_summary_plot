from ROOT import TH1D, TGraph, TGraphAsymmErrors, TCanvas, gStyle, gROOT, gPad
from ROOT import TAttMarker, TAttFill, TColor, TLegend, TText, TLatex
from ROOT import kBlack, kWhite, kBlue, kRed, kGreen, kMagenta, kYellow
from alphaS_CMS import *

# Positions of measurements in categories in the dictionary to be used below
WZ = 0
tt_first = 1
tt_last = 3
jet_first = 4
jet_last = 12
PDG = 13

# Create list with all graphs and legends
Nvalues = len(alpha_S)
graphs = []
legends = []
el = Nvalues + 1
for a in alpha_S:
    # y values with no physical meaning only for drawing (Vector boson: upper, PDG: lower)
    y = np.array([float(el)])  
    y_er = np.array([0.])
                            # npoints        x          y       x_error down   x_error up  y_error down  y_error up
    gr = TGraphAsymmErrors(     1,       a["val"],      y,       a["er_dn"],   a["er_up"],     y_er,        y_er     )
    # Different marker styles based on order
    if(a["order"] == "NLO"):
       gr.SetMarkerStyle(21)
       gr.SetMarkerSize(1.5)
    elif(a["order"] == "NNLO"):
       gr.SetMarkerStyle(22) 
       gr.SetMarkerSize(2)
    elif(a["order"] == "NNLL"):
       gr.SetMarkerStyle(23)
       gr.SetMarkerSize(2)
    else:
       gr.SetMarkerStyle(20)
       gr.SetMarkerSize(1.5)
    
    gr.SetLineWidth(2)
    graphs.append(gr)
    legends.append(a["obs"] + a["sqrts"] + " : " + a["ref"] + " " + a["year"])
    el -= 1 # Index putting the measurements from top to bottom

# Error band for PDG (only 1 point with PDG value and down y error the height of the histogram)
grPDG = TGraphAsymmErrors(1, np.array([0.1180]), np.array([float(Nvalues+1.2)]), np.array([0.0009]), np.array([0.0009]), np.array([float(Nvalues+1.2)]), np.array([0.0]) )
grPDG.SetFillColor(kYellow-7)
grPDG.SetFillStyle(3001)

# Different color style based on the category
# WZ
graphs[WZ].SetMarkerColor(kGreen+2)
graphs[WZ].SetLineColor(kGreen+2)
# ttbar 
for g in range(tt_first,tt_last+1):
    graphs[g].SetMarkerColor(kBlue+1)
    graphs[g].SetLineColor(kBlue+1)
# Jets
for g in range(jet_first,jet_last+1):
    graphs[g].SetMarkerColor(kRed+1)
    graphs[g].SetLineColor(kRed+1)
# PDG
graphs[PDG].SetMarkerColor(kBlack)
graphs[PDG].SetLineColor(kBlack)
  
# dummy histo/graph to make drawing easier
h = TH1D("", "", 100, 0.088, 0.128)
dummy = TGraph(h)
dummy.SetMinimum(1.0)
dummy.SetMaximum(Nvalues + 3)
dummy.GetYaxis().SetLabelSize(0.)
dummy.GetYaxis().SetTickLength(0.)
dummy.GetXaxis().SetTitle("#alpha_{s}(M_{Z}^{2})");
dummy.GetXaxis().SetTitleSize(0.04)
dummy.GetXaxis().SetLabelSize(0.025)
dummy.GetXaxis().SetTitleOffset(1.12)

# Canvas
canv = TCanvas("alpha_S", "alpha_S", 1000, 1600)
dummy.Draw()
grPDG.Draw("2 same") # This is the PDG band
for g in graphs:
    g.Draw("P same")

# Legends with observables and references
xy = [ 0.005, 0.748,  0.4, 0.848 ]
leg = []
for l in range(len(legends)):
    leg.append(TLegend(xy[0],xy[1],xy[2],xy[3]))
    leg[l].AddEntry(legends[l],legends[l], "")
    leg[l].SetTextFont(62)
    leg[l].SetTextSize(0.018)
    leg[l].SetFillColor(kWhite)
    leg[l].SetLineColor(kWhite)
    leg[l].SetBorderSize(0)
    leg[l].SetFillStyle(0)
    xy[1] -= 0.05
    xy[3] -= 0.05

# Different color style based on the category
# WZ
leg[WZ].SetTextColor(kGreen+2)
# ttbar 
for g in range(tt_first,tt_last+1):
    leg[g].SetTextColor(kBlue+1)
# Jets
for g in range(jet_first,jet_last+1):
    leg[g].SetTextColor(kRed+1)

# Draw all the legends
for l in range(len(legends)):
    leg[l].Draw()

# Legends at the top showing the orders
# NLO
leg1 = TLegend(0.20,0.87,0.30,0.90)
leg1.AddEntry(graphs[3]," ", "p")
leg1.SetFillColor(kWhite)
leg1.SetLineColor(kWhite)
leg1.SetBorderSize(0)
leg1.SetFillStyle(0)
leg1.Draw()

leg2 = TLegend(0.22,0.87,0.35,0.90)
leg2.AddEntry(graphs[4]," NLO", "p")
leg2.SetTextSize(0.022)
leg2.SetTextFont(62)
leg2.SetFillColor(kWhite)
leg2.SetLineColor(kWhite)
leg2.SetBorderSize(0)
leg2.SetFillStyle(0)
leg2.Draw()

# NNLL
leg3 = TLegend(0.43,0.87,0.53,0.90)
leg3.AddEntry(graphs[11],"  NNLL", "p")
leg3.SetTextSize(0.022)
leg3.SetTextFont(62)
leg3.SetFillColor(kWhite)
leg3.SetLineColor(kWhite)
leg3.SetBorderSize(0)
leg3.SetFillStyle(0)
leg3.Draw()

# NNLO
leg4 = TLegend(0.62,0.87,0.72,0.90)
leg4.AddEntry(graphs[0]," ", "p")
leg4.SetFillColor(kWhite)
leg4.SetLineColor(kWhite)
leg4.SetBorderSize(0)
leg4.SetFillStyle(0)
leg4.Draw()

leg5 = TLegend(0.65,0.87,0.72,0.90)
leg5.AddEntry(graphs[1]," ", "p")
leg5.SetFillColor(kWhite)
leg5.SetLineColor(kWhite)
leg5.SetBorderSize(0)
leg5.SetFillStyle(0)
leg5.Draw()

leg6 = TLegend(0.68,0.87,0.72,0.90)
leg6.AddEntry(graphs[10],"   NNLO", "p")
leg6.SetTextSize(0.022)
leg6.SetTextFont(62)
leg6.SetFillColor(kWhite)
leg6.SetLineColor(kWhite)
leg6.SetBorderSize(0)
leg6.SetFillStyle(0)
leg6.Draw()

# Text showing the different categories of observables on the right
t00 = TLatex()
t00.SetTextAlign(11)
t00.SetTextSize(0.03)
t00.SetTextColor(kGreen+2)
t00.SetTextAngle(270)
t00.DrawLatexNDC(0.87, 0.84, "Vector")

t01 = TLatex()
t01.SetTextAlign(11)
t01.SetTextSize(0.03)
t01.SetTextColor(kGreen+2)
t01.SetTextAngle(270)
t01.DrawLatexNDC(0.84, 0.84, "boson")

t2 = TLatex()
t2.SetTextAlign(11)
t2.SetTextSize(0.03)
t2.SetTextColor(kBlue+1)
t2.SetTextAngle(270)
t2.DrawLatexNDC(0.855, 0.70, "t#bar{t}")

t3 = TLatex()
t3.SetTextAlign(11)
t3.SetTextSize(0.03)
t3.SetTextColor(kRed+1)
t3.SetTextAngle(270)
t3.DrawLatexNDC(0.855, 0.40, "Jets")

canv.Update()

canv.SaveAs("alpha_S.pdf")
