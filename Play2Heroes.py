disabled rule("============== NOTES SWITCH THE GAME MODE YOU WANT ON ==================")
{
	event
	{
		Ongoing - Global;
	}
}

disabled rule("============= VANILLA : Hero Limits OFF ==========")
{
	event
	{
		Ongoing - Global;
	}
}

disabled rule("Switch")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		(Is Alive(Event Player) && Event Player.C <= 0 && Is Button Held(Event Player, Button(Interact)) && Event Player.B) == True;
		(Has Status(Event Player, Hacked) || Has Status(Event Player, Asleep) || Has Status(Event Player, Knocked Down) || Has Status(
			Event Player, Frozen)) == False;
	}

	actions
	{
		Destroy HUD Text(Event Player.K);
		Event Player.W = Speed Of(Event Player);
		Event Player.V = Velocity Of(Event Player);
		Play Effect(All Players(All Teams), Ring Explosion, Color(White), Position Of(Event Player), 6);
		Play Effect(All Players(All Teams), Good Pickup Effect, Color(White), Position Of(Event Player), 1);
		Play Effect(All Players(All Teams), Ring Explosion Sound, Color(Yellow), Position Of(Event Player), 10);
		Event Player.A = Hero Of(Event Player);
		Event Player.H = 1 - Normalized Health(Event Player);
		Event Player.Q = Ultimate Charge Percent(Event Player);
		Start Forcing Player To Be Hero(Event Player, Event Player.B);
		Event Player.C = Event Player.D + 0.500;
		Chase Player Variable Over Time(Event Player, C, 0, Event Player.C, Destination and Duration);
		Apply Impulse(Event Player, Event Player.V, Event Player.W, To World, Incorporate Contrary Motion);
		Wait(0.100, Ignore Condition);
		Event Player.B = Event Player.A;
		Event Player.A = Hero Of(Event Player);
		Damage(Event Player, Null, Event Player.H * Max Health(Event Player));
		Stop Forcing Player To Be Hero(Event Player);
		Event Player.P = Remove From Array(All Heroes, Event Player.B);
		Set Player Allowed Heroes(Event Player, Event Player.P);
		Wait(0.100, Ignore Condition);
		Create HUD Text(Event Player, Hero Icon String(Event Player.B), String("{0} {1}", String("Cooldown"), Event Player.D), String(
			"{0} {1}", Event Player.B, Event Player.C), Left, 0, Color(Blue), Color(Blue), Color(White), Visible To and String,
			Default Visibility);
		Event Player.K = Last Text ID;
		Set Ultimate Charge(Event Player, Event Player.Q);
		Preload Hero(Event Player, Event Player.B);
		Play Effect(All Players(All Teams), Buff Explosion Sound, Color(White), Event Player, 20);
		Play Effect(All Players(All Teams), Buff Explosion Sound, Color(White), Event Player, 20);
		Event Player.R = False;
	}
}

disabled rule("Reserve Hero (Start of game)")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		(Is In Spawn Room(Event Player) && Is Alive(Event Player) && Event Player.B == Null) == True;
	}

	actions
	{
		Event Player.B = Hero Of(Event Player);
		Event Player.P = Remove From Array(Allowed Heroes(Event Player), Hero Of(Event Player));
		Start Forcing Player To Be Hero(Event Player, Random Value In Array(Event Player.P));
		Wait(0.250, Ignore Condition);
		Stop Forcing Player To Be Hero(Event Player);
		Create HUD Text(Event Player, Hero Icon String(Event Player.B), String("{0} {1}", String("Cooldown"), Event Player.D), String(
			"{0} {1}", Event Player.B, Event Player.C), Left, 0, Color(Blue), Color(Blue), Color(White), Visible To and String,
			Default Visibility);
		Event Player.K = Last Text ID;
		Set Player Allowed Heroes(Event Player, Event Player.P);
	}
}

disabled rule("============== COMP : TEAM HERO LIMIT  =============")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Team 1: On Join Set Available Heroes")
{
	event
	{
		Player Joined Match;
		Team 1;
		All;
	}

	actions
	{
		Set Player Allowed Heroes(Event Player, Global.Y);
	}
}

rule("Team 1: On First Spawn Reserve Hero")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		All;
	}

	conditions
	{
		(Is In Spawn Room(Event Player) && Is Alive(Event Player) && Event Player.B == Null) == True;
	}

	actions
	{
		Event Player.B = Hero Of(Event Player);
		Modify Global Variable(Y, Remove From Array By Value, Hero Of(Event Player));
		Start Forcing Player To Be Hero(Event Player, Random Value In Array(Global.Y));
		Wait(0.250, Ignore Condition);
		Stop Forcing Player To Be Hero(Event Player);
		Create HUD Text(Event Player, Hero Icon String(Event Player.B), String("{0} {1}", String("Cooldown"), Event Player.D), String(
			"{0} {1}", Event Player.B, Event Player.C), Left, 0, Color(Blue), Color(Blue), Color(White), Visible To and String,
			Default Visibility);
		Event Player.K = Last Text ID;
		Event Player.A = Hero Of(Event Player);
		Set Player Allowed Heroes(Event Player, Global.Y);
		Event Player.T = 1;
	}
}

rule("Team 1: Switch (Hero Pool (Y))")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		All;
	}

	conditions
	{
		(Is Alive(Event Player) && Event Player.C <= 0 && Is Button Held(Event Player, Button(Interact)) && Event Player.B) == True;
		(Has Status(Event Player, Hacked) || Has Status(Event Player, Asleep) || Has Status(Event Player, Knocked Down) || Has Status(
			Event Player, Frozen)) == False;
	}

	actions
	{
		Destroy HUD Text(Event Player.K);
		Event Player.W = Speed Of(Event Player);
		Event Player.V = Velocity Of(Event Player);
		Event Player.H = 1 - Normalized Health(Event Player);
		Event Player.Q = Ultimate Charge Percent(Event Player);
		Play Effect(All Players(All Teams), Ring Explosion, Color(White), Position Of(Event Player), 6);
		Play Effect(All Players(All Teams), Good Pickup Effect, Color(White), Position Of(Event Player), 1);
		Play Effect(All Players(All Teams), Ring Explosion Sound, Color(Yellow), Position Of(Event Player), 10);
		Event Player.A = Hero Of(Event Player);
		Modify Global Variable(Y, Remove From Array By Value, Event Player.B);
		Start Forcing Player To Be Hero(Event Player, Event Player.B);
		Event Player.C = Event Player.D + 0.500;
		Chase Player Variable Over Time(Event Player, C, 0, Event Player.C, Destination and Duration);
		Apply Impulse(Event Player, Event Player.V, Event Player.W, To World, Incorporate Contrary Motion);
		Wait(0.100, Ignore Condition);
		Modify Global Variable(Y, Append To Array, Event Player.B);
		Event Player.B = Event Player.A;
		Event Player.A = Hero Of(Event Player);
		Damage(Event Player, Null, Event Player.H * Max Health(Event Player));
		Stop Forcing Player To Be Hero(Event Player);
		Wait(0.100, Ignore Condition);
		Modify Global Variable(Y, Remove From Array By Value, Event Player.B);
		Set Player Allowed Heroes(Event Player, Global.Y);
		Set Ultimate Charge(Event Player, Event Player.Q);
		Preload Hero(Empty Array, Event Player.A + Event Player.B);
		Play Effect(All Players(All Teams), Buff Explosion Sound, Color(White), Event Player, 20);
		Play Effect(All Players(All Teams), Buff Explosion Sound, Color(White), Event Player, 20);
		Create HUD Text(Event Player, Hero Icon String(Event Player.B), String("{0} {1}", String("Cooldown"), Event Player.D), String(
			"{0} {1}", Event Player.B, Event Player.C), Left, 0, Color(Blue), Color(Blue), Color(White), Visible To and String,
			Default Visibility);
		Event Player.K = Last Text ID;
		Event Player.R = False;
	}
}

rule("Team 1: On Leave Start Audit")
{
	event
	{
		Player Left Match;
		Team 1;
		All;
	}

	actions
	{
		Global.W = All Players(Team 1);
		Global.Y = All Heroes;
	}
}

rule("Team 1: Audit List (Players list (W))")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		All;
	}

	conditions
	{
		Array Contains(Global.W, Event Player) == True;
	}

	actions
	{
		Modify Global Variable(W, Remove From Array By Value, Event Player);
		Modify Global Variable(Y, Remove From Array By Value, Event Player.B);
	}
}

rule("Team 1: On Team Switch ReAduit")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		All;
	}

	conditions
	{
		Event Player.T != 1;
	}

	actions
	{
		Event Player.T = 1;
		Event Player.A = Null;
		Event Player.B = Null;
		Event Player.T = Null;
		Event Player.Q = 0;
		Global.W = All Players(Team 1);
		Global.Y = All Heroes;
		Destroy HUD Text(Event Player.K);
	}
}

rule("Team 2: On Join Set Available Heroes")
{
	event
	{
		Player Joined Match;
		Team 2;
		All;
	}

	actions
	{
		Set Player Allowed Heroes(Event Player, Global.Z);
	}
}

rule("Team 2: On First Spawn Reserve Hero")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		All;
	}

	conditions
	{
		(Is In Spawn Room(Event Player) && Is Alive(Event Player) && Event Player.B == Null) == True;
	}

	actions
	{
		Event Player.B = Hero Of(Event Player);
		Modify Global Variable(Z, Remove From Array By Value, Hero Of(Event Player));
		Start Forcing Player To Be Hero(Event Player, Random Value In Array(Global.Z));
		Wait(0.250, Ignore Condition);
		Stop Forcing Player To Be Hero(Event Player);
		Create HUD Text(Event Player, Hero Icon String(Event Player.B), String("{0} {1}", String("Cooldown"), Event Player.D), String(
			"{0} {1}", Event Player.B, Event Player.C), Left, 0, Color(Blue), Color(Blue), Color(White), Visible To and String,
			Default Visibility);
		Event Player.K = Last Text ID;
		Event Player.A = Hero Of(Event Player);
		Set Player Allowed Heroes(Event Player, Global.Z);
		Event Player.T = 1;
	}
}

rule("Team 2: Switch (Hero Pool (Z))")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		All;
	}

	conditions
	{
		(Is Alive(Event Player) && Event Player.C <= 0 && Is Button Held(Event Player, Button(Interact)) && Event Player.B) == True;
		(Has Status(Event Player, Hacked) || Has Status(Event Player, Asleep) || Has Status(Event Player, Knocked Down) || Has Status(
			Event Player, Frozen)) == False;
	}

	actions
	{
		Destroy HUD Text(Event Player.K);
		Event Player.W = Speed Of(Event Player);
		Event Player.V = Velocity Of(Event Player);
		Event Player.H = 1 - Normalized Health(Event Player);
		Event Player.Q = Ultimate Charge Percent(Event Player);
		Play Effect(All Players(All Teams), Ring Explosion, Color(White), Position Of(Event Player), 6);
		Play Effect(All Players(All Teams), Good Pickup Effect, Color(White), Position Of(Event Player), 1);
		Play Effect(All Players(All Teams), Ring Explosion Sound, Color(Yellow), Position Of(Event Player), 10);
		Event Player.A = Hero Of(Event Player);
		Modify Global Variable(Z, Remove From Array By Value, Event Player.B);
		Start Forcing Player To Be Hero(Event Player, Event Player.B);
		Event Player.C = Event Player.D + 0.500;
		Chase Player Variable Over Time(Event Player, C, 0, Event Player.C, Destination and Duration);
		Apply Impulse(Event Player, Event Player.V, Event Player.W, To World, Incorporate Contrary Motion);
		Wait(0.100, Ignore Condition);
		Modify Global Variable(Z, Append To Array, Event Player.B);
		Event Player.B = Event Player.A;
		Event Player.A = Hero Of(Event Player);
		Damage(Event Player, Null, Event Player.H * Max Health(Event Player));
		Stop Forcing Player To Be Hero(Event Player);
		Wait(0.100, Ignore Condition);
		Modify Global Variable(Z, Remove From Array By Value, Event Player.B);
		Set Player Allowed Heroes(Event Player, Global.Z);
		Set Ultimate Charge(Event Player, Event Player.Q);
		Preload Hero(Empty Array, Event Player.A + Event Player.B);
		Play Effect(All Players(All Teams), Buff Explosion Sound, Color(White), Event Player, 20);
		Play Effect(All Players(All Teams), Buff Explosion Sound, Color(White), Event Player, 20);
		Create HUD Text(Event Player, Hero Icon String(Event Player.B), String("{0} {1}", String("Cooldown"), Event Player.D), String(
			"{0} {1}", Event Player.B, Event Player.C), Left, 0, Color(Blue), Color(Blue), Color(White), Visible To and String,
			Default Visibility);
		Event Player.K = Last Text ID;
		Event Player.R = False;
	}
}

rule("Team 2: On Leave Start Audit")
{
	event
	{
		Player Left Match;
		Team 2;
		All;
	}

	actions
	{
		Global.X = All Players(Team 2);
		Global.Z = All Heroes;
	}
}

rule("Team 2: Audit List (Players list (X))")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		All;
	}

	conditions
	{
		Array Contains(Global.W, Event Player) == True;
	}

	actions
	{
		Modify Global Variable(W, Remove From Array By Value, Event Player);
		Modify Global Variable(Y, Remove From Array By Value, Event Player.B);
	}
}

rule("Team 2: On Team Switch ReAduit")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		All;
	}

	conditions
	{
		Event Player.T != 1;
	}

	actions
	{
		Event Player.T = 1;
		Event Player.A = Null;
		Event Player.B = Null;
		Event Player.T = Null;
		Event Player.Q = 0;
		Global.W = All Players(Team 1);
		Global.Y = All Heroes;
		Destroy HUD Text(Event Player.K);
	}
}

disabled rule("============== TIER STUFF ==============")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Build Lists (TIER / Playable Heroes)")
{
	event
	{
		Ongoing - Global;
	}

	conditions
	{
		Global.T == Null;
	}

	actions
	{
		Global.A = Hero(Baptiste);
		Global.A = Append To Array(Global.A, Hero(Sombra));
		Global.A = Append To Array(Global.A, Hero(Reaper));
		Global.B = Hero(Roadhog);
		Global.B = Append To Array(Global.B, Hero(Reinhardt));
		Global.B = Append To Array(Global.B, Hero(Winston));
		Global.B = Append To Array(Global.B, Hero(Wrecking Ball));
		Global.B = Append To Array(Global.B, Hero(D.Va));
		Global.B = Append To Array(Global.B, Hero(Zarya));
		Global.B = Append To Array(Global.B, Hero(Moira));
		Global.B = Append To Array(Global.B, Hero(Brigitte));
		Global.B = Append To Array(Global.B, Hero(Mei));
		Global.B = Append To Array(Global.B, Hero(Lúcio));
		Global.B = Append To Array(Global.B, Hero(Genji));
		Global.B = Append To Array(Global.B, Hero(Hanzo));
		Global.B = Append To Array(Global.B, Hero(Doomfist));
		Global.B = Append To Array(Global.B, Hero(Cassidy));
		Global.B = Append To Array(Global.B, Hero(Pharah));
		Global.C = Hero(Orisa);
		Global.C = Append To Array(Global.C, Hero(Ashe));
		Global.C = Append To Array(Global.C, Hero(Soldier: 76));
		Global.C = Append To Array(Global.C, Hero(Bastion));
		Global.C = Append To Array(Global.C, Hero(Widowmaker));
		Global.C = Append To Array(Global.C, Hero(Tracer));
		Global.C = Append To Array(Global.C, Hero(Junkrat));
		Global.C = Append To Array(Global.C, Hero(Torbjörn));
		Global.C = Append To Array(Global.C, Hero(Mercy));
		Global.C = Append To Array(Global.C, Hero(Ana));
		Global.D = Hero(Symmetra);
		Global.D = Append To Array(Global.D, Hero(Zenyatta));
		Global.T = True;
		Global.Y = All Heroes;
		Global.Z = All Heroes;
	}
}

rule("A TIER HERO (10 seconds)")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Array Contains(Global.A, Event Player.B) == True;
	}

	actions
	{
		Event Player.D = 10;
	}
}

rule("B TIER HERO (8 SECONDS)")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Array Contains(Global.B, Event Player.B) == True;
	}

	actions
	{
		Event Player.D = 8;
	}
}

rule("C TIER HERO (8 SECONDS)")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Array Contains(Global.C, Event Player.B) == True;
	}

	actions
	{
		Event Player.D = 7;
	}
}

rule("D Tier Hero (5 Seconds)")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Array Contains(Global.D, Event Player.B) == True;
	}

	actions
	{
		Event Player.D = 5;
	}
}

disabled rule("============== OPTIONAL CONDITIONS (Default: ON) ==============")
{
	event
	{
		Ongoing - Global;
	}
}

rule("SAFETY: Use Ultimate, change cooldown to 1 second")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Using Ultimate(Event Player) == True;
	}

	actions
	{
		Event Player.C = 1;
		Chase Player Variable Over Time(Event Player, C, 0, Event Player.C, Destination and Duration);
		Destroy HUD Text(Event Player.K);
		Create HUD Text(Event Player, Hero Icon String(Event Player.B), String("{0} {1}", String("Critical"), String("Cooldown")), String(
			"{0} {1} {2}", Event Player.B, Event Player.C, String("!")), Left, 0, Color(Green), Color(Green), Color(White),
			Visible To and String, Default Visibility);
		Event Player.K = Last Text ID;
		Event Player.R = False;
	}
}

rule("If Hacked Reveal Alternative Hero")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Has Status(Event Player, Hacked) == True;
	}

	actions
	{
		Create In-World Text(All Players(All Teams), String("{0} - {1}", Hero Icon String(Event Player.B), Event Player.C), Event Player,
			1, Clip Against Surfaces, Visible To Position and String, Color(White), Default Visibility);
		Event Player.U = Last Text ID;
		Wait(6, Ignore Condition);
		Destroy In-World Text(Event Player.U);
	}
}

rule("On Kill Reset Cooldown")
{
	event
	{
		Player Dealt Final Blow;
		All;
		All;
	}

	actions
	{
		Event Player.C = -1 * Event Player.C;
		Stop Chasing Player Variable(Event Player, C);
	}
}

rule("On Assisst Reduce cooldown")
{
	event
	{
		Player Earned Elimination;
		All;
		All;
	}

	actions
	{
		Stop Chasing Player Variable(Event Player, C);
		Event Player.C = Event Player.C / 2;
		Chase Player Variable Over Time(Event Player, C, 0, Event Player.C, Destination and Duration);
	}
}

rule("Reset Cooldown in spawn room")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		(Is In Spawn Room(Event Player) && Event Player.C > 0) == True;
	}

	actions
	{
		Event Player.C = 0;
	}
}

rule("Special Condition DVA (CD 12 seconds)")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		(Hero Of(Event Player) == Hero(D.Va) && Has Status(Event Player, Invincible)) == True;
	}

	actions
	{
		Stop Chasing Player Variable(Event Player, C);
		Event Player.C = 12;
		Chase Player Variable Over Time(Event Player, C, 0, Event Player.C, Destination and Duration);
	}
}

rule("Special Condition : If Sombra/Bastion")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Hero Of(Event Player) == Hero(Sombra);
		Event Player.B == Hero(Bastion);
		Is Using Ability 1(Event Player) == True;
	}

	actions
	{
		Destroy In-World Text(Event Player.U);
		Create In-World Text(All Players(All Teams), String("{0} - {1}", Hero Icon String(Event Player.B), Event Player.C), Event Player,
			1, Clip Against Surfaces, Visible To Position and String, Color(White), Default Visibility);
		Event Player.U = Last Text ID;
	}
}

rule("Sombra Decloak : Return to normal")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Hero Of(Event Player) == Hero(Sombra);
		Is Using Ability 1(Event Player) == False;
	}

	actions
	{
		Destroy In-World Text(Event Player.U);
	}
}

rule("Change hero KEEP ULTIMATE CHARGE")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		(Event Player.A != Hero Of(Event Player)) == True;
		Event Player.Q > 0;
		Is In Spawn Room(Event Player) == True;
	}

	actions
	{
		Set Ultimate Charge(Event Player, Event Player.Q);
	}
}

disabled rule("============== UI ==============")
{
	event
	{
		Ongoing - Global;
	}
}

rule("UI : Cooldowns to READY")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Event Player.C == 0;
		Event Player.R == False;
		Is In Spawn Room(Event Player) == False;
	}

	actions
	{
		Event Player.R = True;
		Destroy HUD Text(Event Player.K);
		Create HUD Text(Event Player, Hero Icon String(Event Player.B), String("{0} {1}", String("Cooldown"), String("Ready")), String(
			"{0} {1} {2}", Event Player.B, String("Ready"), String("!")), Left, 0, Color(Blue), Color(Blue), Color(White),
			Visible To and String, Default Visibility);
		Event Player.K = Last Text ID;
	}
}

rule("Signature")
{
	event
	{
		Ongoing - Global;
	}

	actions
	{
		Create In-World Text(All Players(All Teams), String("{0} {1}", 2, String("Heroes")), Vector(-31.573, 16.227, -65.612), 3,
			Clip Against Surfaces, Visible To Position and String, Color(White), Default Visibility);
	}
}

disabled rule("============== THIRD PERSON SET UP BY MORNEDIL#2772 ==============")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Turn off Camera")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Event Player.P == True;
		Is Button Held(Event Player, Button(Interact)) == True;
	}

	actions
	{
		Wait(5, Abort When False);
		Event Player.P = False;
	}
}

rule("Turn On Camera")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Event Player.P == False;
		Is Button Held(Event Player, Button(Interact)) == True;
	}

	actions
	{
		Wait(5, Abort When False);
		Event Player.P = True;
	}
}

rule("First-Person Camera - T = False")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Event Player.P == False;
	}

	actions
	{
		Stop Camera(Event Player);
	}
}

rule("Third-Person Camera - T = True  - Awesome Camera by Mornedil#2772 (activated)")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Event Player.P == True;
	}

	actions
	{
		disabled Start Camera(Event Player, Event Player + World Vector Of(Vector(-3 * 0, 0.500, -1), Event Player, Rotation)
			+ Up * 2 + Facing Direction Of(Event Player) * -3, Event Player + Up * 1.500 + Facing Direction Of(Event Player) * 50, 100);
		disabled Wait(0.250, Ignore Condition);
		Start Camera(Event Player, Facing Direction Of(Event Player) * 0.200 + Ray Cast Hit Position(Eye Position(Event Player),
			Eye Position(Event Player) + World Vector Of(Vector(Event Player.S[2], Event Player.S[3], Event Player.S[4]), Event Player,
			Rotation) + Facing Direction Of(Event Player) * Vector(Event Player.S[0], Event Player.S[0] * Event Player.S[1],
			Event Player.S[0]) * -1, All Players(All Teams), Event Player, True), Eye Position(Event Player) + World Vector Of(Vector(
			Event Player.S[2], Event Player.S[3], Event Player.S[4]), Event Player, Rotation) + Facing Direction Of(Event Player) * 500,
			50);
	}
}

rule("camera settings - s,0 = distance ,, s1 = vertical aim multiplier ,, S,2,3,4 = Offset x,y,z  - Awesome Camera by Mornedil#2772")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	actions
	{
		Event Player.S[0] = 3;
		Event Player.S[1] = 1;
		Event Player.S[2] = 0;
		Event Player.S[3] = 0.750;
		Event Player.S[4] = 0;
	}
}