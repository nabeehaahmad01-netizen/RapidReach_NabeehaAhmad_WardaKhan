"""
╔══════════════════════════════════════════════════════════════════╗
║           RapidReach – Emergency Assistance System  v2           ║
║                                                                  ║
║   A Project by  Nabeeha Ahmad  &  Warda Khan                     ║
║   Department of Physics and Applied Mathematics                  ║
║   PIEAS – Pakistan Institute of Engineering & Applied Sciences   ║
╚══════════════════════════════════════════════════════════════════╝

HOW TO RUN
──────────
  Option A – Native desktop window (recommended):
      pip install pywebview
      python RapidReach_v2.py

  Option B – Opens in your default web browser:
      python RapidReach_v2.py --browser

  Option C – Auto-selects best available method:
      python RapidReach_v2.py
"""

import sys, os, tempfile, webbrowser, textwrap

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>RapidReach – Emergency Assistance System</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500;700&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #060810;
  --bg2: #0a0d18;
  --surface: #0e1120;
  --surface2: #141728;
  --surface3: #1a1e30;
  --glass: rgba(255,255,255,0.03);
  --glass2: rgba(255,255,255,0.06);
  --glass3: rgba(255,255,255,0.09);
  --red: #ff3348;
  --red2: #e01030;
  --red3: #ff6070;
  --redglow: rgba(255,51,72,0.3);
  --amber: #ffb020;
  --amber2: #ffd060;
  --amberglow: rgba(255,176,32,0.25);
  --green: #00e07a;
  --blue: #4080ff;
  --text: #eeeaf5;
  --text2: #a8a4b8;
  --muted: #5a566a;
  --border: rgba(255,255,255,0.07);
  --border2: rgba(255,255,255,0.12);
  --r-xs: 8px;
  --r-sm: 12px;
  --r-md: 16px;
  --r-lg: 20px;
  --r-xl: 28px;
}

*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}

html,body{
  height:100%; background:var(--bg);
  color:var(--text); font-family:'Outfit',sans-serif;
  overflow:hidden;
}

/* ── ANIMATED MESH BACKGROUND ── */
.mesh-bg{
  position:fixed;inset:0;z-index:0;pointer-events:none;
  overflow:hidden;
}
.mesh-orb{
  position:absolute;border-radius:50%;filter:blur(100px);
  animation:orbFloat 20s ease-in-out infinite alternate;
}
.orb1{width:700px;height:700px;top:-200px;left:-200px;
  background:radial-gradient(circle,rgba(255,51,72,0.15) 0%,transparent 65%);
  animation-duration:18s;}
.orb2{width:600px;height:600px;bottom:-150px;right:-150px;
  background:radial-gradient(circle,rgba(64,128,255,0.1) 0%,transparent 65%);
  animation-duration:22s;animation-direction:alternate-reverse;}
.orb3{width:400px;height:400px;top:40%;left:40%;
  background:radial-gradient(circle,rgba(255,176,32,0.07) 0%,transparent 65%);
  animation-duration:25s;}
@keyframes orbFloat{
  0%{transform:translate(0,0) scale(1);}
  33%{transform:translate(60px,-40px) scale(1.05);}
  66%{transform:translate(-30px,50px) scale(0.95);}
  100%{transform:translate(40px,20px) scale(1.02);}
}

/* Grid overlay */
.grid-overlay{
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(255,255,255,0.018) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,255,255,0.018) 1px,transparent 1px);
  background-size:60px 60px;
  mask-image:radial-gradient(ellipse 80% 80% at 50% 50%,black 40%,transparent 100%);
}

/* ── SPLASH ── */
#splash{
  position:fixed;inset:0;z-index:200;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  background:var(--bg);
  transition:opacity 1s ease,visibility 1s ease;
}
#splash.hidden{opacity:0;visibility:hidden;pointer-events:none;}

.splash-ring{
  position:relative;width:110px;height:110px;
  animation:splashIn 0.8s cubic-bezier(0.34,1.56,0.64,1) both;
}
.splash-ring-outer{
  position:absolute;inset:-12px;border-radius:50%;
  border:1px solid rgba(255,51,72,0.3);
  animation:spinSlow 8s linear infinite;
}
.splash-ring-outer::after{
  content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);
  width:6px;height:6px;border-radius:50%;background:var(--red);
  box-shadow:0 0 10px var(--red);
}
.splash-ring-mid{
  position:absolute;inset:-5px;border-radius:50%;
  border:1px dashed rgba(255,176,32,0.2);
  animation:spinSlow 12s linear infinite reverse;
}
.splash-logo-box{
  width:110px;height:110px;border-radius:24px;
  background:linear-gradient(135deg,var(--red2),var(--red));
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 0 60px var(--redglow),0 0 120px rgba(255,51,72,0.1),inset 0 1px 0 rgba(255,255,255,0.15);
  position:relative;overflow:hidden;
}
.splash-logo-box::before{
  content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;
  background:conic-gradient(transparent 0deg,rgba(255,255,255,0.08) 180deg,transparent 360deg);
  animation:spinSlow 4s linear infinite;
}
.splash-logo-text{
  font-family:'Syne',sans-serif;font-size:30px;font-weight:800;
  color:#fff;letter-spacing:1px;position:relative;z-index:1;
}
@keyframes spinSlow{to{transform:rotate(360deg);}}
@keyframes splashIn{from{transform:scale(0.3) rotate(-15deg);opacity:0;}to{transform:scale(1) rotate(0deg);opacity:1;}}

.splash-wordmark{
  font-family:'Syne',sans-serif;font-weight:800;
  font-size:clamp(56px,9vw,88px);letter-spacing:-1px;
  margin-top:30px;line-height:1;
  background:linear-gradient(135deg,#fff 30%,rgba(255,255,255,0.5));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  animation:fadeSlideUp 0.6s 0.4s ease both;
}
.splash-wordmark span{
  background:linear-gradient(135deg,var(--red) 0%,var(--amber) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}

.splash-tag{
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:4px;
  color:var(--muted);text-transform:uppercase;margin-top:8px;
  animation:fadeSlideUp 0.6s 0.55s ease both;
}

.splash-sep{
  width:1px;height:60px;
  background:linear-gradient(180deg,transparent,var(--red),transparent);
  margin:32px auto;
  animation:fadeSlideUp 0.6s 0.65s ease both;
}

.splash-by{
  font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:3px;
  color:var(--red);text-transform:uppercase;margin-bottom:16px;
  animation:fadeSlideUp 0.6s 0.7s ease both;
}

.splash-cards{
  display:flex;gap:16px;flex-wrap:wrap;justify-content:center;
  animation:fadeSlideUp 0.6s 0.75s ease both;
}
.splash-card{
  background:var(--glass2);border:1px solid var(--border2);
  border-radius:var(--r-md);padding:14px 24px;
  backdrop-filter:blur(20px);position:relative;overflow:hidden;
}
.splash-card::before{
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.15),transparent);
}
.splash-card-name{
  font-family:'Syne',sans-serif;font-size:18px;font-weight:700;
  color:var(--text);letter-spacing:0.5px;
}
.splash-card-dept{font-size:11px;color:var(--text2);margin-top:4px;letter-spacing:0.3px;}

.splash-inst{
  margin-top:18px;
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:2px;
  color:var(--amber);animation:fadeSlideUp 0.6s 0.85s ease both;
}

.splash-btn{
  margin-top:36px;
  position:relative;padding:16px 52px;
  background:transparent;border:1px solid var(--border2);
  border-radius:var(--r-md);cursor:pointer;overflow:hidden;
  font-family:'JetBrains Mono',monospace;font-size:11px;
  letter-spacing:4px;text-transform:uppercase;color:var(--text);
  transition:color 0.3s,border-color 0.3s,transform 0.2s;
  animation:fadeSlideUp 0.6s 0.95s ease both;
}
.splash-btn::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,var(--red2),var(--red));
  transform:translateX(-100%);transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);
}
.splash-btn:hover{border-color:var(--red);color:#fff;transform:scale(1.02);}
.splash-btn:hover::before{transform:translateX(0);}
.splash-btn span{position:relative;z-index:1;}
.splash-btn:active{transform:scale(0.97);}

@keyframes fadeSlideUp{from{opacity:0;transform:translateY(22px);}to{opacity:1;transform:translateY(0);}}

/* ── APP WRAPPER ── */
#app{
  position:fixed;inset:0;z-index:10;
  display:flex;flex-direction:column;overflow:hidden;
  opacity:0;transition:opacity 0.7s ease;
}
#app.visible{opacity:1;}

/* ── HEADER ── */
.header{
  display:flex;align-items:center;justify-content:space-between;
  padding:0 24px;height:62px;
  background:rgba(10,13,24,0.85);backdrop-filter:blur(30px);
  border-bottom:1px solid var(--border);flex-shrink:0;
  position:relative;z-index:50;
}
.header::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent 0%,var(--red) 30%,transparent 100%);
  opacity:0.4;
}
.h-left{display:flex;align-items:center;gap:14px;}
.h-logo{
  width:36px;height:36px;border-radius:10px;
  background:linear-gradient(135deg,var(--red2),var(--red));
  display:flex;align-items:center;justify-content:center;
  font-family:'Syne',sans-serif;font-size:12px;font-weight:800;
  box-shadow:0 0 20px var(--redglow);flex-shrink:0;
  position:relative;overflow:hidden;
}
.h-logo::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(255,255,255,0.15),transparent);
}
.h-name{
  font-family:'Syne',sans-serif;font-size:18px;font-weight:800;
  letter-spacing:0.5px;line-height:1;
}
.h-sub{
  font-family:'JetBrains Mono',monospace;font-size:8px;
  letter-spacing:2px;color:var(--muted);margin-top:3px;text-transform:uppercase;
}
.h-right{display:flex;align-items:center;gap:16px;}
.h-status{
  display:flex;align-items:center;gap:7px;
  font-family:'JetBrains Mono',monospace;font-size:9px;
  color:var(--green);letter-spacing:1px;
  background:rgba(0,224,122,0.07);border:1px solid rgba(0,224,122,0.15);
  border-radius:20px;padding:5px 12px;
}
.s-dot{
  width:6px;height:6px;border-radius:50%;background:var(--green);
  box-shadow:0 0 8px var(--green);
  animation:statusPulse 2s ease-in-out infinite;
}
@keyframes statusPulse{
  0%,100%{opacity:1;transform:scale(1);}
  50%{opacity:0.5;transform:scale(0.8);}
}

/* Search bar in header */
.h-search{
  display:flex;align-items:center;gap:8px;
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-sm);padding:7px 14px;
  transition:border-color 0.2s,background 0.2s;
  min-width:220px;
}
.h-search:focus-within{
  border-color:rgba(255,51,72,0.4);
  background:var(--surface2);
}
.h-search-icon{font-size:13px;color:var(--muted);flex-shrink:0;}
.h-search input{
  background:none;border:none;outline:none;
  font-family:'Outfit',sans-serif;font-size:12px;color:var(--text);
  width:100%;
}
.h-search input::placeholder{color:var(--muted);}

/* ── SCROLL AREA ── */
.scroll-area{
  flex:1;overflow-y:auto;overflow-x:hidden;
  padding:28px;position:relative;z-index:10;
  scroll-behavior:smooth;
}
.scroll-area::-webkit-scrollbar{width:3px;}
.scroll-area::-webkit-scrollbar-track{background:transparent;}
.scroll-area::-webkit-scrollbar-thumb{background:var(--surface3);border-radius:3px;}
.scroll-area:hover::-webkit-scrollbar-thumb{background:var(--muted);}

/* ── BREADCRUMB ── */
.breadcrumb{
  display:flex;align-items:center;gap:8px;margin-bottom:24px;
  flex-wrap:wrap;
}
.bc-item{
  font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;
  color:var(--muted);cursor:pointer;transition:color 0.2s;
  padding:4px 0;
}
.bc-item:hover{color:var(--text);}
.bc-item.active{color:var(--red);cursor:default;}
.bc-sep{color:var(--muted);font-size:10px;}

/* ── PAGE SYSTEM ── */
.page{display:none;}
.page.active{display:block;animation:pageIn 0.35s ease both;}
@keyframes pageIn{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:translateY(0);}}

/* ── HOME PAGE ── */
.hero-band{
  display:flex;align-items:center;justify-content:space-between;
  margin-bottom:32px;flex-wrap:wrap;gap:16px;
}
.hero-text{}
.hero-label{
  font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:4px;
  color:var(--red);text-transform:uppercase;margin-bottom:10px;
  display:flex;align-items:center;gap:8px;
}
.hero-label::before{
  content:'';width:20px;height:1px;background:var(--red);
}
.hero-h1{
  font-family:'Syne',sans-serif;font-size:clamp(32px,4vw,48px);
  font-weight:800;line-height:1.05;letter-spacing:-0.5px;
}
.hero-h1 em{
  font-style:normal;
  background:linear-gradient(90deg,var(--red),var(--amber));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.hero-desc{
  font-size:13px;color:var(--text2);margin-top:10px;
  font-weight:300;max-width:500px;line-height:1.6;
}

/* Stats row */
.stats-row{
  display:flex;gap:12px;flex-wrap:wrap;margin-bottom:32px;
}
.stat-chip{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-sm);padding:12px 18px;
  display:flex;align-items:center;gap:10px;
  flex:1;min-width:130px;
}
.stat-num{
  font-family:'Syne',sans-serif;font-size:24px;font-weight:800;
  line-height:1;
}
.stat-num.red{color:var(--red);}
.stat-num.amber{color:var(--amber);}
.stat-num.green{color:var(--green);}
.stat-label{font-size:11px;color:var(--text2);font-weight:300;}

/* Category grid */
.cat-grid{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(280px,1fr));
  gap:12px;
}
.cat-card{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-lg);padding:22px;cursor:pointer;
  position:relative;overflow:hidden;
  transition:transform 0.3s cubic-bezier(0.34,1.56,0.64,1),
             border-color 0.3s,box-shadow 0.3s;
  animation:cardIn 0.4s ease both;
}
@keyframes cardIn{from{opacity:0;transform:translateY(18px);}to{opacity:1;transform:translateY(0);}}
.cat-card::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(255,51,72,0.06),transparent 60%);
  opacity:0;transition:opacity 0.3s;
}
.cat-card::after{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,var(--red),var(--amber));
  transform:scaleX(0);transform-origin:left;transition:transform 0.3s ease;
}
.cat-card:hover{
  transform:translateY(-5px);
  border-color:rgba(255,51,72,0.25);
  box-shadow:0 16px 48px rgba(255,51,72,0.1),0 4px 16px rgba(0,0,0,0.4);
}
.cat-card:hover::before{opacity:1;}
.cat-card:hover::after{transform:scaleX(1);}
.cat-card:active{transform:scale(0.98) translateY(-2px);}

.cat-head{
  display:flex;align-items:flex-start;justify-content:space-between;
  margin-bottom:14px;
}
.cat-emoji{font-size:28px;line-height:1;filter:drop-shadow(0 2px 8px rgba(0,0,0,0.4));}
.cat-index{
  font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;
  color:var(--muted);
  background:var(--surface2);border:1px solid var(--border);
  border-radius:6px;padding:4px 8px;
}
.cat-name{
  font-family:'Syne',sans-serif;font-size:15px;font-weight:700;
  line-height:1.3;margin-bottom:6px;
}
.cat-count{
  font-size:11px;color:var(--muted);
  font-family:'JetBrains Mono',monospace;
}
.cat-arrow{
  display:flex;align-items:center;justify-content:space-between;
  margin-top:16px;padding-top:14px;border-top:1px solid var(--border);
}
.cat-arrow-icon{
  font-size:13px;color:var(--muted);
  transition:transform 0.2s,color 0.2s;
}
.cat-card:hover .cat-arrow-icon{color:var(--red);transform:translateX(4px);}
.cat-progress{
  flex:1;height:2px;background:var(--border);
  border-radius:2px;margin-right:12px;overflow:hidden;
}
.cat-progress-fill{
  height:100%;border-radius:2px;
  background:linear-gradient(90deg,var(--red),var(--amber));
  width:0%;transition:width 1s ease 0.3s;
}

/* ── SEARCH RESULTS ── */
.search-header{
  font-family:'JetBrains Mono',monospace;font-size:10px;
  letter-spacing:2px;color:var(--muted);margin-bottom:16px;
  text-transform:uppercase;
}
.search-result{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-md);padding:16px 20px;margin-bottom:8px;
  display:flex;align-items:center;gap:14px;cursor:pointer;
  transition:all 0.2s;
}
.search-result:hover{
  background:var(--surface2);border-color:rgba(255,51,72,0.25);
  transform:translateX(4px);
}
.sr-path{
  font-family:'JetBrains Mono',monospace;font-size:9px;
  color:var(--muted);letter-spacing:1px;
  display:flex;align-items:center;gap:4px;margin-bottom:4px;
}
.sr-name{font-size:14px;font-weight:500;}
.sr-match{color:var(--amber);}
.sr-icon{font-size:20px;flex-shrink:0;}
.sr-arrow{color:var(--muted);margin-left:auto;flex-shrink:0;}

/* ── SUB PAGE ── */
.sub-hero{
  display:flex;align-items:center;gap:20px;
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-lg);padding:22px 26px;margin-bottom:24px;
  position:relative;overflow:hidden;
}
.sub-hero::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(255,51,72,0.04),transparent);
}
.sub-hero-emoji{font-size:44px;filter:drop-shadow(0 4px 12px rgba(0,0,0,0.4));flex-shrink:0;}
.sub-hero-title{
  font-family:'Syne',sans-serif;font-size:clamp(18px,3vw,26px);
  font-weight:800;letter-spacing:-0.3px;position:relative;z-index:1;
}
.sub-hero-desc{
  font-size:12px;color:var(--text2);margin-top:5px;
  font-weight:300;position:relative;z-index:1;
}

.sub-grid{display:flex;flex-direction:column;gap:8px;}
.sub-row{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-sm);padding:16px 20px;
  display:flex;align-items:center;gap:14px;cursor:pointer;
  transition:all 0.25s;animation:cardIn 0.35s ease both;
  position:relative;overflow:hidden;
}
.sub-row::before{
  content:'';position:absolute;left:0;top:0;bottom:0;width:3px;
  background:linear-gradient(180deg,var(--red),var(--amber));
  transform:scaleY(0);transition:transform 0.2s ease;
}
.sub-row:hover{
  background:var(--surface2);
  border-color:rgba(255,51,72,0.2);
  transform:translateX(6px);
}
.sub-row:hover::before{transform:scaleY(1);}
.sub-n{
  font-family:'JetBrains Mono',monospace;font-size:11px;
  color:var(--muted);min-width:32px;flex-shrink:0;
}
.sub-name{font-size:14px;font-weight:500;flex:1;}
.sub-tags{display:flex;gap:6px;flex-wrap:wrap;}
.sub-tag{
  font-family:'JetBrains Mono',monospace;font-size:9px;
  letter-spacing:1px;color:var(--muted);
  background:var(--surface3);border:1px solid var(--border);
  border-radius:4px;padding:2px 7px;
}
.sub-arr{color:var(--muted);transition:color 0.2s,transform 0.2s;}
.sub-row:hover .sub-arr{color:var(--red);transform:translateX(4px);}

/* ── INFO PAGE ── */
.info-layout{display:grid;grid-template-columns:1fr;gap:16px;}
@media(min-width:800px){.info-layout{grid-template-columns:1.6fr 1fr;}}

.info-main{}
.info-top{
  background:linear-gradient(135deg,var(--red2) 0%,#8b0010 100%);
  border-radius:var(--r-lg) var(--r-lg) 0 0;
  padding:28px;position:relative;overflow:hidden;
}
.info-top::before{
  content:'';position:absolute;top:-60px;right:-60px;
  width:250px;height:250px;border-radius:50%;
  background:rgba(255,255,255,0.05);
}
.info-top::after{
  content:'';position:absolute;bottom:-80px;left:-30px;
  width:200px;height:200px;border-radius:50%;
  background:rgba(0,0,0,0.15);
}
.info-top-label{
  font-family:'JetBrains Mono',monospace;font-size:8px;
  letter-spacing:3px;color:rgba(255,255,255,0.5);
  text-transform:uppercase;margin-bottom:10px;position:relative;z-index:1;
}
.info-title{
  font-family:'Syne',sans-serif;font-size:clamp(22px,4vw,34px);
  font-weight:800;position:relative;z-index:1;line-height:1.1;
  letter-spacing:-0.3px;
}

.info-body{
  background:var(--surface);
  border-radius:0 0 var(--r-lg) var(--r-lg);
  border:1px solid var(--border);border-top:none;
  padding:24px;
}

.sec-label{
  font-family:'JetBrains Mono',monospace;font-size:8px;
  letter-spacing:3px;color:var(--red);text-transform:uppercase;
  margin-bottom:12px;display:flex;align-items:center;gap:8px;
}
.sec-label::after{content:'';flex:1;height:1px;background:var(--border);}

.steps-container{display:flex;flex-direction:column;gap:6px;}
.step{
  display:flex;align-items:flex-start;gap:12px;
  padding:12px 14px;border-radius:var(--r-xs);
  border:1px solid transparent;
  transition:background 0.2s,border-color 0.2s;
  animation:stepIn 0.3s ease both;
}
.step:hover{background:var(--glass);border-color:var(--border);}
.step.warn{
  background:rgba(255,176,32,0.04);
  border-color:rgba(255,176,32,0.12);
}
.step.warn:hover{background:rgba(255,176,32,0.08);}

.step-num{
  font-family:'JetBrains Mono',monospace;font-size:9px;
  color:var(--muted);min-width:20px;flex-shrink:0;
  padding-top:3px;
}
.step-icon{font-size:14px;flex-shrink:0;padding-top:1px;}
.step-text{font-size:13px;line-height:1.55;flex:1;}
.step-text.w{color:var(--amber);font-weight:500;}

@keyframes stepIn{from{opacity:0;transform:translateX(-8px);}to{opacity:1;transform:translateX(0);}}

/* Side panel */
.info-side{}
.contacts-card{
  background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r-lg);overflow:hidden;position:sticky;top:0;
}
.contacts-card-head{
  background:linear-gradient(135deg,rgba(255,51,72,0.15),rgba(255,51,72,0.05));
  border-bottom:1px solid var(--border);
  padding:16px 20px;
  font-family:'JetBrains Mono',monospace;font-size:9px;
  letter-spacing:3px;color:var(--red);text-transform:uppercase;
}
.contact-list{padding:12px;}
.contact-item{
  display:flex;align-items:center;gap:12px;
  padding:12px 14px;border-radius:var(--r-xs);
  margin-bottom:6px;
  background:var(--surface2);border:1px solid var(--border);
  cursor:pointer;transition:all 0.2s;
  position:relative;overflow:hidden;
}
.contact-item:last-child{margin-bottom:0;}
.contact-item::before{
  content:'';position:absolute;left:0;top:0;bottom:0;width:3px;
  background:var(--red);transform:scaleY(0);
  transition:transform 0.2s;
}
.contact-item:hover{border-color:rgba(255,51,72,0.3);}
.contact-item:hover::before{transform:scaleY(1);}
.c-icon{
  width:34px;height:34px;border-radius:var(--r-xs);
  background:rgba(255,51,72,0.12);border:1px solid rgba(255,51,72,0.2);
  display:flex;align-items:center;justify-content:center;
  font-size:15px;flex-shrink:0;
}
.c-num{
  font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:700;
  color:var(--text);
}
.c-name{font-size:10px;color:var(--muted);margin-top:2px;}

/* Quick tips */
.tip-card{
  background:rgba(255,176,32,0.05);border:1px solid rgba(255,176,32,0.15);
  border-radius:var(--r-lg);padding:18px;margin-top:14px;
}
.tip-head{
  font-family:'JetBrains Mono',monospace;font-size:8px;
  letter-spacing:3px;color:var(--amber);text-transform:uppercase;
  margin-bottom:12px;display:flex;align-items:center;gap:6px;
}
.tip-item{
  display:flex;align-items:flex-start;gap:8px;
  font-size:12px;color:var(--text2);line-height:1.5;margin-bottom:8px;
}
.tip-item:last-child{margin-bottom:0;}
.tip-dot{
  width:5px;height:5px;border-radius:50%;background:var(--amber);
  flex-shrink:0;margin-top:6px;
}

/* ── FOOTER ── */
.footer{
  padding:10px 24px;
  background:rgba(10,13,24,0.9);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
  flex-shrink:0;
}
.footer-left{
  font-family:'JetBrains Mono',monospace;font-size:9px;
  letter-spacing:2px;color:var(--muted);
}
.footer-ticker{
  font-family:'JetBrains Mono',monospace;font-size:9px;
  color:var(--red);letter-spacing:1px;
  display:flex;align-items:center;gap:6px;
}
.ticker-dot{
  width:5px;height:5px;border-radius:50%;background:var(--red);
  animation:statusPulse 1.5s ease-in-out infinite;
}
</style>
</head>
<body>

<!-- Backgrounds -->
<div class="mesh-bg">
  <div class="mesh-orb orb1"></div>
  <div class="mesh-orb orb2"></div>
  <div class="mesh-orb orb3"></div>
</div>
<div class="grid-overlay"></div>

<!-- SPLASH -->
<div id="splash">
  <div class="splash-ring">
    <div class="splash-ring-outer"></div>
    <div class="splash-ring-mid"></div>
    <div class="splash-logo-box"><div class="splash-logo-text">RR</div></div>
  </div>
  <div class="splash-wordmark">Rapid<span>Reach</span></div>
  <div class="splash-tag">Emergency Assistance System</div>
  <div class="splash-sep"></div>
  <div class="splash-by">A Project By</div>
  <div class="splash-cards">
    <div class="splash-card">
      <div class="splash-card-name">Nabeeha Ahmad</div>
      <div class="splash-card-dept">Physics &amp; Applied Mathematics</div>
    </div>
    <div class="splash-card">
      <div class="splash-card-name">Warda Khan</div>
      <div class="splash-card-dept">Physics &amp; Applied Mathematics</div>
    </div>
  </div>
  <div class="splash-inst">PIEAS — Pakistan Institute of Engineering &amp; Applied Sciences</div>
  <button class="splash-btn" onclick="enterApp()"><span>Enter System →</span></button>
</div>

<!-- APP -->
<div id="app">
  <div class="header">
    <div class="h-left">
      <div class="h-logo">RR</div>
      <div>
        <div class="h-name">RapidReach</div>
        <div class="h-sub">Emergency Assistance System</div>
      </div>
    </div>
    <div class="h-right">
      <div class="h-search">
        <div class="h-search-icon">⌕</div>
        <input id="searchInput" type="text" placeholder="Search emergencies..." oninput="onSearch(this.value)" />
      </div>
      <div class="h-status"><div class="s-dot"></div>LIVE</div>
    </div>
  </div>

  <div class="scroll-area" id="scrollArea">

    <!-- HOME PAGE -->
    <div id="page-home" class="page active">
      <div class="hero-band">
        <div class="hero-text">
          <div class="hero-label">Emergency Response</div>
          <div class="hero-h1">Select an<br><em>Emergency</em> Category</div>
          <div class="hero-desc">Guided step-by-step response procedures with Pakistan emergency contacts for any crisis situation.</div>
        </div>
      </div>
      <div class="stats-row" id="statsRow"></div>
      <div class="cat-grid" id="catGrid"></div>
    </div>

    <!-- SEARCH RESULTS PAGE -->
    <div id="page-search" class="page">
      <div class="breadcrumb" id="srBreadcrumb"></div>
      <div class="search-header" id="srHeader"></div>
      <div id="srResults"></div>
    </div>

    <!-- SUBS PAGE -->
    <div id="page-subs" class="page">
      <div class="breadcrumb" id="subsBreadcrumb"></div>
      <div class="sub-hero" id="subsHero"></div>
      <div class="sub-grid" id="subGrid"></div>
    </div>

    <!-- INFO PAGE -->
    <div id="page-info" class="page">
      <div class="breadcrumb" id="infoBreadcrumb"></div>
      <div class="info-layout" id="infoLayout"></div>
    </div>

  </div>

  <div class="footer">
    <div class="footer-left">Stay calm · Provide accurate location · RapidReach</div>
    <div class="footer-ticker"><div class="ticker-dot"></div>Emergency services available 24/7</div>
  </div>
</div>

<script>
// ─── DATA ───
const CATS = [
  {id:1,emoji:"🚑",name:"Ambulance / Medical",full:"Ambulance & Medical Services"},
  {id:2,emoji:"🚔",name:"Police / Law Enforcement",full:"Police & Law Enforcement"},
  {id:3,emoji:"🚒",name:"Fire Brigade / Rescue",full:"Fire Brigade & Rescue"},
  {id:4,emoji:"🌊",name:"Disaster & Rescue",full:"Disaster & Rescue Services"},
  {id:5,emoji:"🛣️",name:"Motorway & Transport",full:"Motorway & Transport Authorities"},
  {id:6,emoji:"🤝",name:"Social Protection",full:"Social Protection Helplines"},
  {id:7,emoji:"🐾",name:"Animal & Specialized",full:"Animal & Specialized Services"},
  {id:8,emoji:"⚡",name:"Utility & Infrastructure",full:"Utility & Infrastructure Services"},
];
const SUBS = {
  1:["Cardiac Arrest / Heart Attack","Respiratory Distress / Choking","Poisoning & Overdose","Snake or Insect Bites","Road Traffic Accident","Blood Bank & Organ Donation","Mental Health & Suicide Prevention"],
  2:["Theft / Armed Robbery","Cyber Crime & Online Fraud","Missing Persons","Domestic Violence","Terrorism / Suspicious Activity","Workplace Harassment"],
  3:["Fire Emergency","Forest Fires","Chemical Spills","Gas Leakage","Electrical Short Circuit / Fallen Wires","Structure Collapse / Building Fall"],
  4:["Flood & Water Logging","Earthquake Response","Large-Scale Building Collapse","Water Rescue / Drowning"],
  5:["Highway / Motorway Breakdown","Road Traffic Accident (RTA)","Railway Emergency","Airport / Aviation Security","Elevator / Lift Malfunction"],
  6:["Women Helpline / Domestic Violence","Child Protection / Child Abuse","Missing Child","Elderly Care Services"],
  7:["Animal Cruelty & Rescue","Dead Body Transport / Mortuary Services"],
  8:["Major Water Leakage","Sewerage Overflow / Blockage","Total Power Grid Failure","Gas Supply Emergency"],
};
const INFO = {
  "1,1":{title:"Cardiac Arrest / Heart Attack",contacts:[{num:"1122 / 115",name:"Emergency Rescue"}],steps:[["Check the area is safe before approaching.",false],["Tap and shout to check responsiveness.",false],["If no response, call 1122 / 115 immediately.",false],["Check breathing for up to 10 seconds.",false],["If not breathing, start CPR immediately.",false],["Lay person flat on a firm surface.",false],["Place hands center of chest, push hard and fast.",false],["Push at least 2 inches deep at 100–120 per minute.",false],["Allow full chest recoil between compressions.",false],["If trained: 2 rescue breaths after every 30 compressions.",false],["Use AED immediately if available.",false],["Continue until help arrives or person breathes normally.",false],["Do NOT stop CPR unless absolutely necessary.",true],["Do NOT give food, water, or medication.",true]],tip:["Time is critical — every second counts in cardiac arrest","AEDs are found in airports, malls, and large buildings","Hands-only CPR (no breaths) is effective for untrained bystanders"]},
  "1,2":{title:"Respiratory Distress / Choking",contacts:[{num:"1122 / 115",name:"Emergency Rescue"}],steps:[["Check if person can speak, cough, or breathe.",false],["If they can cough, encourage strong coughing.",false],["If breathing difficult, call 1122 / 115 immediately.",false],["If unable to speak/breathe — severe choking.",false],["Stand behind person, wrap arms around waist.",false],["Fist above navel, grasp with other hand.",false],["Give quick inward-upward thrusts (Heimlich).",false],["Repeat until object is expelled or person goes unconscious.",false],["If unconscious, lower to ground and start CPR.",false],["Check airway between compressions.",false],["For infants: back blows and chest thrusts only.",false],["Do NOT put fingers blindly into the mouth.",true],["Do NOT give food or water during choking.",true]],tip:["Lean person slightly forward when applying back blows","Ask bystanders to call emergency while you perform Heimlich","Different technique required for pregnant women — chest thrusts only"]},
  "1,3":{title:"Poisoning & Overdose",contacts:[{num:"1122 / 115",name:"Emergency Rescue"}],steps:[["Call 1122 / 115 immediately.",false],["Check consciousness and breathing.",false],["If unconscious but breathing: recovery position.",false],["If not breathing: start CPR if trained.",false],["Identify poison: medicine, chemical, or gas.",false],["Keep container/label to show medical staff.",false],["If inhaled gas: move to fresh air immediately.",false],["If on skin: remove contaminated clothing, wash with water.",false],["Keep person calm and still.",false],["Stay with them until help arrives.",false],["Do NOT induce vomiting unless told by professionals.",true],["Do NOT give food, drink, or medicine.",true]],tip:["Time of ingestion and amount taken is critical info for doctors","Household chemicals are a leading cause of poisoning","Carbon monoxide is odorless — get CO detectors for your home"]},
  "1,4":{title:"Snake or Insect Bites",contacts:[{num:"1122 / 115",name:"Emergency Rescue"}],steps:[["Call 1122 / 115 immediately.",false],["Keep person calm and still.",false],["Limit movement to slow venom spread.",false],["Keep bitten area at or below heart level.",false],["Remove rings, watches, tight items before swelling.",false],["Clean bite gently with water if possible.",false],["Cover with clean, loose bandage.",false],["Note time of bite and symptoms.",false],["Try to remember snake/insect appearance (safely).",false],["Watch for swelling, difficulty breathing, dizziness.",false],["Do NOT cut wound or suck out venom.",true],["Do NOT apply ice, chemicals, or tourniquet.",true]],tip:["Most snakebite deaths are preventable with prompt antivenom","Keep person lying flat — elevation can speed venom absorption","Antivenom is available at major hospitals"]},
  "1,5":{title:"Road Traffic Accident",contacts:[{num:"1122 / 115",name:"Emergency Rescue"}],steps:[["Ensure your own safety first.",false],["Move to safe area away from traffic.",false],["Call 1122 / 115 — give exact location.",false],["Turn on hazard lights or warn vehicles.",false],["Check injured persons: consciousness, breathing.",false],["If heavily bleeding, apply firm pressure.",false],["Keep injured person still and calm.",false],["If unconscious but breathing: recovery position.",false],["If not breathing and trained: start CPR.",false],["Stay until emergency services arrive.",false],["Do NOT move seriously injured people unless fire/danger.",true],["Do NOT remove helmets unless breathing is blocked.",true],["Do NOT give food, water, or medication.",true]],tip:["Always keep an emergency triangle in your vehicle","Having blood type noted on ID can speed treatment","Golden Hour — first 60 min are most critical for trauma"]},
  "1,6":{title:"Blood Bank & Organ Donation",contacts:[{num:"1122 / 115",name:"Emergency Rescue"}],steps:[["Call 1122 or contact hospital immediately.",false],["Confirm required blood group and units needed.",false],["Contact nearby blood banks or transfusion services.",false],["Ask family/friends or verified donors for urgent help.",false],["Share: patient name, hospital, blood group, urgency.",false],["Keep doctor's prescription or hospital slip ready.",false],["Ensure donor is healthy and meets criteria.",false],["For organ donation: inform hospital staff immediately.",false],["Consent from family/legal guardians is required.",false],["Do NOT trust unknown or illegal paid donors.",true],["Do NOT delay in emergencies.",true]],tip:["O-negative is universal donor blood type","Organ donation must be registered and family informed","Pakistan has severe blood shortage — consider becoming a regular donor"]},
  "1,7":{title:"Mental Health & Suicide Prevention",contacts:[{num:"1122 / 115",name:"Emergency Rescue"},{num:"15",name:"Police"}],steps:[["Stay with the person and ensure immediate safety.",false],["Speak calmly, listen without judging.",false],["Encourage them to talk about how they feel.",false],["Remove sharp objects, medicines, harmful items.",false],["If immediate risk: call 1122 / 115 or Police 15.",false],["Reassure them help is available and they're not alone.",false],["Encourage contact with trusted family/friend.",false],["Keep them in a safe comfortable environment.",false],["Stay until professional help arrives.",false],["Do NOT leave person alone if suicide risk is high.",true],["Do NOT ignore warning signs or delay help.",true],["Do NOT argue, threaten, or judge.",true]],tip:["Asking about suicide does NOT increase risk — ask directly","Listen more, advise less — presence is more powerful than words","Follow up after crisis — recovery takes ongoing support"]},
  "2,1":{title:"Theft / Armed Robbery",contacts:[{num:"15",name:"Police"}],steps:[["Stay calm — do not resist if robber is armed.",true],["Hand over valuables if demanded.",false],["Avoid sudden movements or arguing.",true],["Stay observant without staring directly.",false],["Note details: face, clothing, voice, vehicle.",false],["Move to safe area as soon as possible.",false],["Call Police 15 immediately.",false],["Note time, location, direction suspect escaped.",false],["Cooperate fully with police when they arrive.",false],["Do NOT chase the suspect.",true],["Do NOT disturb crime scene or touch evidence.",true]],tip:["Your safety is more valuable than any possession","Try to memorize one identifying detail clearly","Security cameras on your route can help police"]},
  "2,2":{title:"Cyber Crime & Online Fraud",contacts:[{num:"1799",name:"Cyber Crime Wing"}],steps:[["Do NOT share OTP, PIN, passwords, or bank details.",true],["Stop communication with suspected scammer.",false],["Screenshot messages, numbers, links, transactions.",false],["Save all evidence: emails, receipts, call logs.",false],["Contact bank or mobile wallet to block transactions.",false],["Change passwords of affected accounts immediately.",false],["Enable two-factor authentication.",false],["Report to Cyber Crime helpline: 1799.",false],["Do NOT click unknown links or download suspicious files.",true],["Do NOT delete evidence before reporting.",true]],tip:["Legitimate banks NEVER ask for OTP via call or SMS","Enable 2FA on all important accounts immediately","Report fraud within 24hrs for best chance of recovery"]},
  "2,3":{title:"Missing Persons",contacts:[{num:"15",name:"Police"}],steps:[["Call Police 15 immediately — do not wait.",false],["Share: recent photo, clothing, age, last seen location.",false],["Check nearby: home, school, workplace, relatives.",false],["Contact friends, neighbors, and known contacts.",false],["Visit or call nearby hospitals and police stations.",false],["Ask nearby shops for CCTV footage.",false],["Keep phone available for police contact.",false],["Do NOT delay reporting or assume they will return.",true]],tip:["The first 24-48 hours are most critical for finding missing persons","Have a recent clear photo of loved ones available","NADRA can assist in locating persons via national ID"]},
  "2,4":{title:"Domestic Violence",contacts:[{num:"15",name:"Police"},{num:"1099",name:"Women Helpline"}],steps:[["If in immediate danger: call Police 15.",false],["Move to safe place or public area.",false],["Contact Women Helpline 1099 for support.",false],["Inform trusted friend, family, or neighbor.",false],["Keep important items ready: phone, ID, money.",false],["Save evidence: photos, messages, medical reports.",false],["Plan a safe exit route if situation worsens.",false],["Do NOT confront abuser alone.",true],["Do NOT stay in life-threatening situation.",true]],tip:["Safety planning saves lives — have a plan before you need it","Children witnessing domestic violence are also victims","Legal aid is available free of charge through district courts"]},
  "2,5":{title:"Suspicious Activity / Terrorism",contacts:[{num:"15",name:"Police"}],steps:[["Move away from area calmly without panic.",false],["Call Police 15 — report exact location.",false],["Note: person, behavior, object, vehicle, timing.",false],["Warn others if it can be done safely.",false],["Follow instructions from police/security.",false],["Keep emergency exits in mind.",false],["Do NOT touch or approach suspicious objects.",true],["Do NOT spread rumors or panic messages.",true]],tip:["If you see something suspicious, say something","Unattended bags in public places should always be reported","Do not use mobile phone near suspected explosive device"]},
  "2,6":{title:"Workplace Harassment",contacts:[{num:"15",name:"Police"}],steps:[["Remove yourself from situation if possible.",false],["Tell the person to stop if safe to do so.",false],["Document: dates, times, messages, witnesses.",false],["Save evidence: emails, chats, recordings, photos.",false],["Report to HR, supervisor, or relevant authority.",false],["Inform a trusted colleague for support.",false],["If threats, stalking, or assault: call Police 15.",false],["Do NOT ignore repeated behavior.",true],["Do NOT meet harasser alone in isolated places.",true]],tip:["Pakistan has Federal law against workplace harassment (2010)","Keep a private record/diary of all incidents with dates","Ombudsman offices handle workplace harassment complaints"]},
  "3,1":{title:"Fire Emergency",contacts:[{num:"16 / 1122",name:"Fire Brigade"}],steps:[["Call 16 / 1122 — give exact location.",false],["Alert others, start evacuation calmly.",false],["Use stairs only — NEVER elevators.",true],["Stay low to avoid smoke, cover nose/mouth.",false],["Move quickly to nearest safe exit.",false],["Close doors behind you to slow fire spread.",false],["Help children, elderly, injured first if safe.",false],["Once outside: move far from building.",false],["If clothes catch fire: Stop, Drop, and Roll.",false],["Do NOT re-enter the building for any reason.",true],["Do NOT hide inside rooms or bathrooms.",true]],tip:["Practice fire evacuation routes with your family","Feel doors before opening — if hot, use another route","Smoke inhalation is more deadly than flames in most fires"]},
  "3,2":{title:"Forest Fires",contacts:[{num:"16 / 1122",name:"Fire Brigade"}],steps:[["Move away from fire to safe area immediately.",false],["Call 16 / 1122 — report exact location.",false],["Cover nose and mouth with cloth.",false],["Move upwind away from smoke/fire.",false],["Evacuate early if fire is spreading.",false],["Assist children, elderly, injured if safe.",false],["Keep vehicle windows closed while evacuating.",false],["Stay on cleared roads — avoid forest paths.",false],["Do NOT try to fight large fires yourself.",true],["Do NOT stop to take photos or videos.",true],["Do NOT return until declared safe.",true]],tip:["Forest fires spread fastest uphill and with wind","Wet cloth over face filters some smoke particles","Satellite imagery helps track large fire movements in real-time"]},
  "3,3":{title:"Chemical Spills",contacts:[{num:"16 / 1122",name:"Fire Brigade"}],steps:[["Leave area immediately if you smell/see spill.",false],["Move upwind and away from spill.",false],["Warn others calmly.",false],["Call 16 / 1122 — report location and type.",false],["Cover nose/mouth with cloth if exposed.",false],["Remove contaminated clothing if safe.",false],["Wash exposed skin with water.",false],["Keep safe distance until emergency teams arrive.",false],["Do NOT touch, inhale, or step into chemical.",true],["Do NOT try to clean or neutralize it yourself.",true]],tip:["Upwind means away from where the wind is blowing toward","Different chemicals require different decontamination — leave to professionals","If eyes exposed: flush with clean water for 15 minutes minimum"]},
  "3,4":{title:"Gas Leakage",contacts:[{num:"16 / 1122",name:"Fire Brigade"}],steps:[["Do NOT switch on/off any electrical switches.",true],["Do NOT use matches, lighters, or flames.",true],["Open doors and windows slowly to ventilate.",false],["Turn off main gas valve if safe.",false],["Evacuate immediately to safe distance.",false],["Warn others calmly to leave.",false],["Call 16 / 1122 from outside the area.",false],["Stay outside until authorities declare safe.",false],["Do NOT use mobile phones inside leak area.",true],["Do NOT create any sparks.",true]],tip:["Gas companies add smell (mercaptan) to odorless natural gas for detection","Gas valve is usually near your gas meter outdoors","If unsure of leak size — evacuate first, call from outside"]},
  "3,5":{title:"Electrical Short Circuit / Fallen Wires",contacts:[{num:"16 / 1122",name:"Fire Brigade"},{num:"118",name:"WAPDA / Electricity Board"}],steps:[["Stay far from fallen wires or sparks.",false],["Warn others to keep safe distance.",false],["Turn off main power only if safe and accessible.",false],["If someone is shocked: do NOT touch until power is off.",true],["Call 16 / 1122 and report location.",false],["Inform electricity authority (WAPDA/LESCO).",false],["Keep children and crowd away from site.",false],["Do NOT touch any wire, pole, or device.",true],["Do NOT attempt to remove fallen wires.",true],["Do NOT use water on electrical fire.",true]],tip:["Current can travel through wet ground near fallen wires","Keep a safe distance of at least 10 meters from fallen lines","LESCO/IESCO have 24-hour emergency fault reporting lines"]},
  "3,6":{title:"Structure Collapse / Building Fall",contacts:[{num:"16 / 1122",name:"Fire Brigade"}],steps:[["Move away from collapsed building immediately.",false],["Warn others to stay clear.",false],["Call 16 / 1122 — report location and trapped people.",false],["If trapped: stay still, avoid kicking up dust.",false],["Cover nose/mouth with cloth or mask.",false],["Tap on pipes or walls to signal rescuers.",false],["Shout only when necessary (conserve energy).",false],["Keep access points clear for rescue teams.",false],["Do NOT enter unstable structures.",true],["Do NOT attempt to move heavy debris.",true],["Do NOT re-enter collapsed structures.",true]],tip:["Void spaces next to sturdy furniture offer best survival spots","Three taps repeatedly is a universal distress signal","Rescuers use listening devices — even faint sounds can be detected"]},
  "4,1":{title:"Flood & Water Logging",contacts:[{num:"051-111-157-157",name:"NDMA"},{num:"1129",name:"PDMA Punjab"},{num:"1736",name:"PDMA Sindh"}],steps:[["Move to higher ground immediately.",false],["Follow official warnings and evacuation orders.",false],["Switch off electricity and gas if safe.",false],["Take essentials: ID, medicine, phone, water.",false],["Keep children, elderly, animals away from floodwater.",false],["Stay away from bridges, drains, fast water.",true],["Do NOT walk or drive through floodwater.",true],["Do NOT touch electrical devices in water.",true],["Do NOT return until declared safe.",true]],tip:["Just 15cm of fast-moving water can knock down an adult","Floodwater is often contaminated with sewage and chemicals","Keep emergency bag packed during monsoon season"]},
  "4,2":{title:"Earthquake Response",contacts:[{num:"051-111-157-157",name:"NDMA"},{num:"1129",name:"PDMA Punjab"}],steps:[["Drop to ground immediately.",false],["Take Cover under sturdy table or interior wall.",false],["Hold On until shaking stops.",false],["Stay away from windows, glass, heavy furniture.",false],["If outside: open ground away from buildings/wires.",false],["If driving: stop safely, stay inside.",false],["After shaking: evacuate carefully via stairs only.",false],["Check yourself and others for injuries.",false],["Be alert for aftershocks.",false],["Avoid damaged buildings and fallen wires.",false],["Do NOT use elevators.",true],["Do NOT re-enter until declared safe.",true]],tip:["Most injuries from earthquakes are from falling objects, not the shaking","Door frames are no longer considered the safest spot — use Drop-Cover-Hold","Pakistan is in a high seismic zone — know your building's safety rating"]},
  "4,3":{title:"Large-Scale Building Collapse",contacts:[{num:"1122",name:"Emergency Rescue"},{num:"051-111-157-157",name:"NDMA"}],steps:[["Move away from collapsed structure immediately.",false],["Warn others to stay clear.",false],["Call 1122 — report location and trapped people.",false],["Keep access routes clear for rescue vehicles.",false],["If trapped: stay calm, conserve energy.",false],["Cover nose/mouth to avoid dust inhalation.",false],["Tap on pipes or walls to signal rescuers.",false],["Do NOT enter unstable or partially collapsed buildings.",true],["Do NOT attempt to move heavy debris.",true],["Do NOT light matches or create sparks.",true]],tip:["Survivors have been rescued days after collapse with modern tools","Noise makers (phone alarm, whistle) help rescuers locate survivors","Heavy equipment arrives within hours — stay calm and signal position"]},
  "4,4":{title:"Water Rescue / Drowning",contacts:[{num:"1122",name:"Emergency Rescue"}],steps:[["Call 1122 immediately — give exact location.",false],["Try to rescue from land: rope, stick, floating object.",false],["Encourage person to grab onto something that floats.",false],["If person brought out unconscious: check breathing.",false],["If not breathing: start CPR immediately.",false],["Continue CPR until emergency help arrives.",false],["Keep person warm and dry after rescue.",false],["Do NOT jump in unless trained and safe.",true],["Do NOT attempt risky entry without equipment.",true]],tip:["Reach-Throw-Don't Go — rescuers say land rescue first always","A drowning person often cannot call for help — watch for silent drowning signs","Swimming pools, rivers, and canals are all drowning risks — supervise children always"]},
  "5,1":{title:"Highway / Motorway Breakdown",contacts:[{num:"130",name:"Motorway Police"}],steps:[["Turn on hazard lights immediately.",false],["Move vehicle to hard shoulder / emergency lane.",false],["Keep passengers behind safety barriers if available.",false],["Place warning triangle behind vehicle if available.",false],["Call 130 — give motorway, direction, km marker, nearest exit.",false],["Stay away from moving traffic.",true],["Do NOT stand on road side of vehicle.",true],["Wait in safe area away from traffic.",false],["Keep emergency numbers and vehicle details ready.",false]],tip:["NHA emergency phones are placed every 2km on motorways","Always carry a reflective triangle and vest","Motorway breakdowns cause serious secondary accidents — light up your vehicle"]},
  "5,2":{title:"Road Traffic Accident (RTA)",contacts:[{num:"1122 / 130 / 15",name:"Emergency Services"}],steps:[["Ensure own safety before approaching.",false],["Turn on hazard lights, warn oncoming traffic.",false],["Call 1122 / 130 / 15 — give exact location.",false],["State number of injured and type of accident.",false],["Check breathing and consciousness of victims.",false],["Control bleeding with firm pressure on clean cloth.",false],["If unconscious but breathing: recovery position.",false],["If not breathing and trained: start CPR.",false],["Stay at scene until emergency services arrive.",false],["Do NOT move seriously injured unless fire/danger.",true],["Do NOT remove helmets unless breathing is blocked.",true]],tip:["Golden Hour — first 60 minutes of trauma are most critical","Keep a first aid kit in your vehicle at all times","Collect witness contact info for insurance/police reports"]},
  "5,3":{title:"Railway Emergency",contacts:[{num:"117",name:"Railway Helpline"},{num:"15",name:"Police"}],steps:[["Move away from tracks immediately.",false],["Warn others to stay clear.",false],["Call 117 or 15 — report location (station, track, direction).",false],["If someone injured near tracks: wait for railway staff.",false],["Follow instructions from railway authorities or police.",false],["Keep children and crowd away.",false],["Do NOT stand or walk on tracks at any time.",true],["Do NOT try to stop or block a moving train.",true],["Do NOT touch electrical railway lines.",true]],tip:["Trains cannot stop quickly — stopping distance can exceed 1km at speed","Level crossings are the most dangerous railway locations","Pakistan Railways operates a 24-hour emergency helpline"]},
  "5,4":{title:"Airport / Aviation Security",contacts:[{num:"114",name:"ASF Airport Security"},{num:"15",name:"Police"}],steps:[["Inform airport security of suspicious activity.",false],["Move away from any unattended bags.",true],["Call 114 or 15 — report exact airport location.",false],["Follow all instructions from security staff.",false],["Keep calm, avoid creating panic.",false],["Keep ID and travel documents ready.",false],["Stay in designated safe areas.",false],["Do NOT touch or move unattended luggage.",true],["Do NOT spread unverified information.",true]],tip:["ASF officers are armed and trained for airport threats","Your boarding pass shows your departure gate zone","Aviation security uses layers — one reported concern triggers full response"]},
  "5,5":{title:"Elevator / Lift Malfunction",contacts:[{num:"Building Security",name:"Maintenance Team"}],steps:[["Stay calm — do not panic.",false],["Press the emergency alarm or help button.",false],["Call building security or maintenance.",false],["Share: building name, floor, lift number.",false],["Use intercom if available.",false],["If phone signal available: call emergency contacts.",false],["Keep children calm and seated.",false],["Do NOT try to force open lift doors.",true],["Do NOT attempt to climb out unless instructed.",true],["Do NOT jump or force movement inside.",true]],tip:["Modern lifts have multiple safety systems — free-fall is extremely rare","Emergency lighting activates automatically in most modern lifts","Trapped time is usually 30–90 minutes with prompt response"]},
  "6,1":{title:"Women Helpline / Domestic Violence",contacts:[{num:"15",name:"Police"},{num:"1099",name:"Women Helpline"}],steps:[["If in immediate danger: call Police 15.",false],["Move to safe place or public area.",false],["Contact Women Helpline 1099 for guidance.",false],["Inform trusted friend, family, or neighbor.",false],["Keep phone charged and accessible.",false],["Save evidence: messages, calls, photos, threats.",false],["Plan safe exit route if situation worsens.",false],["Do NOT ignore repeated harassment or threats.",true],["Do NOT confront alone.",true]],tip:["Women Helpline 1099 provides legal, psychological, and shelter support","Evidence stored digitally (cloud) is safer and harder to destroy","Restraining orders can be obtained through Family Courts"]},
  "6,2":{title:"Child Protection / Child Abuse",contacts:[{num:"1121",name:"Child Protection"},{num:"15",name:"Police"},{num:"1122",name:"Emergency Rescue"}],steps:[["If immediate danger: call 1122 or 15.",false],["Move child to safe environment.",false],["Contact Child Protection Helpline 1121.",false],["Inform trusted adult, guardian, or authority.",false],["If child injured: seek medical help immediately.",false],["Keep child calm and reassure them.",false],["Listen carefully, do not blame or pressure.",false],["Preserve evidence if safe.",false],["Stay with child or ensure trusted adult stays.",false],["Do NOT confront suspected abuser alone.",true],["Do NOT ignore signs of abuse.",true]],tip:["Children rarely lie about abuse — take all disclosures seriously","CPLC Child Protection offices operate in major cities","Medical examination by trained professionals preserves evidence legally"]},
  "6,3":{title:"Missing Child",contacts:[{num:"15",name:"Police"},{num:"1121",name:"Child Protection"}],steps:[["Call Police 15 and Child Protection 1121 immediately.",false],["Do NOT wait — report as soon as child is missing.",true],["Share: recent photo, age, clothing, physical description.",false],["Provide last seen location and time.",false],["Check nearby safe places first.",false],["Ask neighbors and shops for information.",false],["Request CCTV footage from nearby areas.",false],["Keep phone available for police updates.",false],["Do NOT delay reporting hoping child returns.",true]],tip:["Print and distribute flyers within the first hour if possible","Social media can help rapidly spread missing child information","Pakistan Child Tracker Program (PCTP) assists in missing child cases"]},
  "6,4":{title:"Elderly Care Services",contacts:[{num:"1122",name:"Emergency Rescue"},{num:"Family Doctor",name:"Caregiver"}],steps:[["Check consciousness and responsiveness.",false],["If unconscious or not breathing: call 1122.",false],["If fall or injury: do NOT move them.",true],["Keep still and calm to avoid further injury.",false],["Check for breathing, chest pain, stroke signs.",false],["Call medical help for serious symptoms.",false],["Inform family members or caregiver immediately.",false],["Keep medicines and medical history ready.",false],["Provide comfort, warmth, and reassurance.",false],["Do NOT ignore sudden confusion or weakness.",true],["Do NOT give medication without medical advice.",true]],tip:["Stroke warning: Face drooping, Arm weakness, Speech difficulty — call immediately","Hip fractures in elderly often need surgery — do not delay treatment","FAST mnemonic helps identify strokes in time for treatment"]},
  "7,1":{title:"Animal Cruelty & Rescue",contacts:[{num:"1122",name:"Emergency Rescue"},{num:"Local Authority",name:"Animal Rescue"}],steps:[["Keep safe distance from injured/aggressive animal.",false],["Call 1122 or local animal rescue.",false],["Report exact location and animal condition.",false],["Keep children and crowd away.",false],["Avoid provoking or stressing animal further.",false],["If bitten: wash wound with soap and water immediately.",false],["Seek medical attention as soon as possible.",false],["If safe: provide water until help arrives.",false],["Do NOT handle or capture animal yourself.",true],["Do NOT hit, chase, or corner animal.",true]],tip:["Rabies is fatal if untreated — any animal bite needs medical assessment","Stray dog populations are linked to disease spread — report to local authorities","Many cities have veterinary emergency helplines for animal rescue"]},
  "7,2":{title:"Dead Body Transport / Mortuary",contacts:[{num:"1122",name:"Emergency Rescue"},{num:"15",name:"Police (if required)"}],steps:[["Check for breathing or response first.",false],["Call 1122 if death is sudden or unclear.",false],["If suspicious, violent, or accidental: inform Police 15.",false],["Contact hospital, ambulance, or mortuary for transport.",false],["Keep identification documents ready.",false],["Inform close family members immediately.",false],["Follow hospital or legal procedures.",false],["Maintain dignity and respect for deceased.",false],["Do NOT move body until authorities arrive (suspicious death).",true],["Do NOT disturb scene if part of investigation.",true]],tip:["Death certificate is required for burial and legal proceedings","Hospital morgues provide temporary storage with dignity","District courts issue No-Objection Certificates for body transport across provinces"]},
  "8,1":{title:"Major Water Leakage",contacts:[{num:"Local WASA",name:"Water Authority"}],steps:[["Turn off main water supply immediately.",false],["Switch off electricity in affected area if safe.",false],["Move electrical appliances away from water.",false],["Report to local water authority (WASA).",false],["Give exact location and severity of leak.",false],["Keep children and elderly away from area.",false],["Do NOT walk through flooded or slippery areas.",true],["Do NOT touch electrical switches with wet hands.",true]],tip:["Water and electricity are a lethal combination — treat both with caution","WASA emergency teams operate round the clock","Mold begins growing within 24-48 hours of water damage"]},
  "8,2":{title:"Sewerage Overflow / Blockage",contacts:[{num:"Local WASA",name:"Municipal Authority"}],steps:[["Avoid contact with contaminated water.",true],["Keep children and elderly away.",false],["Report to local municipal authority or WASA.",false],["Provide exact location and severity.",false],["Wear boots or gloves if passing nearby.",false],["Wash hands thoroughly if exposed.",false],["Keep doors and nearby drains closed.",false],["Do NOT touch contaminated surfaces bare-handed.",true]],tip:["Sewage water contains pathogens causing cholera, typhoid, and hepatitis","Disinfect any area that comes in contact with sewage water","After contact: wash thoroughly with soap, monitor for 48 hours"]},
  "8,3":{title:"Total Power Grid Failure",contacts:[{num:"118",name:"WAPDA / Electricity Board"}],steps:[["Stay calm, use flashlights or battery lights.",false],["Turn off and unplug sensitive appliances.",false],["Keep refrigerator/freezer closed to preserve food.",false],["Use battery devices for emergency updates.",false],["Check on elderly and people on medical devices.",false],["Report outage to 118 or local electricity provider.",false],["Avoid using elevators.",true],["Do NOT use generators indoors or in closed spaces.",true],["Avoid candles near flammable materials.",true]],tip:["Food stays frozen 24-48 hours in a full, closed freezer","Medical devices users should have backup power or hospital plan","WAPDA outage maps are available on their official app"]},
  "8,4":{title:"Gas Supply Emergency",contacts:[{num:"SSGC / SNGPL",name:"Gas Company"},{num:"16 / 1122",name:"Fire Brigade"}],steps:[["Do NOT switch on/off any electrical switches.",true],["Do NOT use matches, lighters, or open flame.",true],["Open doors and windows slowly to ventilate.",false],["Turn off main gas valve if safe.",false],["Evacuate immediately to safe distance.",false],["Warn others calmly to leave.",false],["Call gas company or emergency from outside.",false],["Stay outside until authorities confirm safe.",false],["Do NOT use mobile phone inside suspected leak area.",true],["Do NOT create any sparks whatsoever.",true]],tip:["Natural gas is lighter than air — it accumulates near ceiling","Propane/LPG is heavier than air — it sinks to floor level","Pakistan's gas emergency line operates 24/7 for pipeline leaks"]},
};

// ─── STATE ───
let currentCat = null;
let searchTimeout = null;

// ─── INIT ───
function enterApp() {
  document.getElementById('splash').classList.add('hidden');
  const app = document.getElementById('app');
  app.classList.add('visible');
  buildHome();
}

function buildHome() {
  // Stats
  const totalSubs = Object.values(SUBS).reduce((a, b) => a + b.length, 0);
  document.getElementById('statsRow').innerHTML = `
    <div class="stat-chip"><div class="stat-num red">${CATS.length}</div><div class="stat-label">Emergency<br>Categories</div></div>
    <div class="stat-chip"><div class="stat-num amber">${totalSubs}</div><div class="stat-label">Emergency<br>Scenarios</div></div>
    <div class="stat-chip"><div class="stat-num green">24/7</div><div class="stat-label">Service<br>Availability</div></div>
    <div class="stat-chip"><div class="stat-num" style="color:var(--blue)">15+</div><div class="stat-label">Helpline<br>Numbers</div></div>
  `;

  // Category cards
  const grid = document.getElementById('catGrid');
  grid.innerHTML = '';
  CATS.forEach((cat, i) => {
    const subCount = (SUBS[cat.id] || []).length;
    const card = document.createElement('div');
    card.className = 'cat-card';
    card.style.animationDelay = (i * 0.05) + 's';
    card.innerHTML = `
      <div class="cat-head">
        <div class="cat-emoji">${cat.emoji}</div>
        <div class="cat-index">0${cat.id}</div>
      </div>
      <div class="cat-name">${cat.full}</div>
      <div class="cat-count">${subCount} emergency scenario${subCount !== 1 ? 's' : ''}</div>
      <div class="cat-arrow">
        <div class="cat-progress"><div class="cat-progress-fill" id="prog-${cat.id}"></div></div>
        <div class="cat-arrow-icon">→</div>
      </div>
    `;
    card.onclick = () => showSubs(cat.id);
    grid.appendChild(card);
  });

  // Animate progress bars
  setTimeout(() => {
    CATS.forEach(cat => {
      const el = document.getElementById('prog-' + cat.id);
      if (el) el.style.width = (((SUBS[cat.id] || []).length / 7) * 100) + '%';
    });
  }, 400);
}

// ─── SEARCH ───
function onSearch(val) {
  clearTimeout(searchTimeout);
  const v = val.trim();
  if (!v) {
    showPage('home');
    return;
  }
  searchTimeout = setTimeout(() => performSearch(v), 180);
}

function performSearch(query) {
  const q = query.toLowerCase();
  const results = [];
  CATS.forEach(cat => {
    (SUBS[cat.id] || []).forEach((subName, idx) => {
      const key = `${cat.id},${idx + 1}`;
      const info = INFO[key];
      let match = subName.toLowerCase().includes(q) || cat.full.toLowerCase().includes(q);
      if (info) {
        info.steps.forEach(s => { if (s[0].toLowerCase().includes(q)) match = true; });
      }
      if (match) results.push({ cat, subName, subIdx: idx + 1, key });
    });
  });

  document.getElementById('srBreadcrumb').innerHTML = buildBreadcrumb([{label:'Home',page:'home'}], 'Search Results');
  document.getElementById('srHeader').textContent = `${results.length} result${results.length !== 1 ? 's' : ''} for "${query}"`;

  const container = document.getElementById('srResults');
  if (results.length === 0) {
    container.innerHTML = `<div style="padding:32px;text-align:center;color:var(--muted)">
      <div style="font-size:32px;margin-bottom:12px">🔍</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:2px;">No results found</div>
    </div>`;
  } else {
    container.innerHTML = results.map((r, i) => `
      <div class="search-result" style="animation-delay:${i*0.04}s;animation:cardIn 0.3s ease both;" onclick="showInfoFromSearch(${r.cat.id},${r.subIdx})">
        <div class="sr-icon">${r.cat.emoji}</div>
        <div style="flex:1">
          <div class="sr-path"><span>${r.cat.name}</span><span>›</span></div>
          <div class="sr-name">${highlightMatch(r.subName, query)}</div>
        </div>
        <div class="sr-arrow">→</div>
      </div>
    `).join('');
  }
  showPage('search');
}

function highlightMatch(text, query) {
  const re = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')})`, 'gi');
  return text.replace(re, '<span class="sr-match">$1</span>');
}

function showInfoFromSearch(catId, subId) {
  currentCat = CATS.find(c => c.id === catId);
  showInfo(catId, subId, 'search');
}

// ─── SUBS ───
function showSubs(catId) {
  const cat = CATS.find(c => c.id === catId);
  currentCat = cat;
  document.getElementById('subsBreadcrumb').innerHTML = buildBreadcrumb([{label:'Home',page:'home'}], cat.full);

  document.getElementById('subsHero').innerHTML = `
    <div class="sub-hero-emoji">${cat.emoji}</div>
    <div>
      <div class="sub-hero-title">${cat.full}</div>
      <div class="sub-hero-desc">${(SUBS[catId]||[]).length} emergency scenarios — select for detailed guidance and contacts</div>
    </div>
  `;

  const grid = document.getElementById('subGrid');
  grid.innerHTML = '';
  (SUBS[catId] || []).forEach((name, i) => {
    const row = document.createElement('div');
    row.className = 'sub-row';
    row.style.animationDelay = (i * 0.04) + 's';
    row.innerHTML = `
      <div class="sub-n">0${i + 1}</div>
      <div class="sub-name">${name}</div>
      <div class="sub-arr">→</div>
    `;
    row.onclick = () => showInfo(catId, i + 1, 'subs');
    grid.appendChild(row);
  });
  showPage('subs');
}

// ─── INFO ───
function showInfo(catId, subId, backTo) {
  const data = INFO[`${catId},${subId}`];
  const cat = CATS.find(c => c.id === catId) || currentCat;

  const backItems = backTo === 'search'
    ? [{label:'Home',page:'home'},{label:'Search',page:'search'}]
    : [{label:'Home',page:'home'},{label:cat.full,page:'subs',catId}];

  document.getElementById('infoBreadcrumb').innerHTML = buildBreadcrumb(backItems, data ? data.title : 'Info');

  const layout = document.getElementById('infoLayout');
  if (!data) {
    layout.innerHTML = '<p style="padding:24px;color:var(--muted)">No data found.</p>';
    showPage('info');
    return;
  }

  const warnSteps = data.steps.filter(s => s[1]);
  const normalSteps = data.steps.filter(s => !s[1]);

  const stepsHTML = data.steps.map((s, i) => `
    <div class="step ${s[1] ? 'warn' : ''}" style="animation-delay:${i * 0.03}s">
      <div class="step-num">${String(i + 1).padStart(2, '0')}</div>
      <div class="step-icon">${s[1] ? '⚠️' : '✓'}</div>
      <div class="step-text ${s[1] ? 'w' : ''}">${s[0]}</div>
    </div>
  `).join('');

  const contactsHTML = data.contacts.map(c => `
    <div class="contact-item">
      <div class="c-icon">📞</div>
      <div>
        <div class="c-num">${c.num}</div>
        <div class="c-name">${c.name}</div>
      </div>
    </div>
  `).join('');

  const tipHTML = data.tip ? `
    <div class="tip-card">
      <div class="tip-head">💡 Quick Tips</div>
      ${data.tip.map(t => `<div class="tip-item"><div class="tip-dot"></div><div>${t}</div></div>`).join('')}
    </div>
  ` : '';

  layout.innerHTML = `
    <div class="info-main">
      <div class="info-top">
        <div class="info-top-label">Emergency Procedure</div>
        <div class="info-title">${data.title}</div>
      </div>
      <div class="info-body">
        <div class="sec-label">Step-by-Step Actions</div>
        <div style="margin-bottom:8px;font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);letter-spacing:1px;">
          ${normalSteps.length} actions · ${warnSteps.length} warnings
        </div>
        <div class="steps-container">${stepsHTML}</div>
      </div>
    </div>
    <div class="info-side">
      <div class="contacts-card">
        <div class="contacts-card-head">Emergency Contacts</div>
        <div class="contact-list">${contactsHTML}</div>
      </div>
      ${tipHTML}
    </div>
  `;
  showPage('info');
}

// ─── UTILS ───
function buildBreadcrumb(items, active) {
  const parts = items.map(item => {
    if (item.catId) {
      return `<span class="bc-item" onclick="showSubs(${item.catId})">${item.label}</span>`;
    }
    return `<span class="bc-item" onclick="showPage('${item.page}')">${item.label}</span>`;
  });
  parts.push(`<span class="bc-sep">›</span><span class="bc-item active">${active}</span>`);
  return parts.join('<span class="bc-sep">›</span>');
}

function showPage(name) {
  if (name === 'home' && document.getElementById('searchInput').value) {
    document.getElementById('searchInput').value = '';
  }
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById('page-' + name).classList.add('active');
  document.getElementById('scrollArea').scrollTop = 0;
}

// Keyboard shortcut: Escape to go back
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    const active = document.querySelector('.page.active');
    if (!active) return;
    const id = active.id;
    if (id === 'page-info') showPage('subs');
    else if (id === 'page-subs') showPage('home');
    else if (id === 'page-search') { document.getElementById('searchInput').value = ''; showPage('home'); }
  }
});
</script>
</body>
</html>"""

APP_TITLE  = "RapidReach – Emergency Assistance System v2"
WIN_WIDTH  = 1200
WIN_HEIGHT = 750

def launch_pywebview():
    import webview
    window = webview.create_window(
        title     = APP_TITLE,
        html      = HTML,
        width     = WIN_WIDTH,
        height    = WIN_HEIGHT,
        min_size  = (800, 580),
        resizable = True,
    )
    webview.start()

def launch_browser():
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(HTML)
    tmp.close()
    url = "file://" + tmp.name.replace("\\", "/")
    print(f"\n  Opening RapidReach v2 in your browser...")
    print(f"  File: {tmp.name}\n")
    webbrowser.open(url)
    try:
        input("  Press ENTER to close and clean up...")
    except (EOFError, KeyboardInterrupt):
        pass
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass

def main():
    banner = textwrap.dedent("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║         RapidReach – Emergency Assistance System  v2             ║
    ║                                                                  ║
    ║  A Project by  Nabeeha Ahmad  &  Warda Khan                      ║
    ║  Department of Physics and Applied Mathematics                   ║
    ║  PIEAS – Pakistan Institute of Engineering & Applied Sciences    ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)
    print(banner)
    force_browser = "--browser" in sys.argv
    if force_browser:
        launch_browser()
        return
    try:
        import webview  # noqa
        print("  [pywebview detected]  Launching native window...\n")
        launch_pywebview()
    except ImportError:
        print("  [pywebview not found]  Falling back to browser.\n")
        print("  TIP: Install pywebview for a native window:")
        print("       pip install pywebview\n")
        launch_browser()

if __name__ == "__main__":
    main()