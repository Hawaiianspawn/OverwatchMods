variables
{
	global:
		19: TeleportRangeFactor

	player:
		26: LocationPrediction
		27: Distance
		28: GunnerMode
		31: Target
		35: Parent
		36: ProjectileSpeed
		37: Child
		38: ProjectileAirTime
		39: PredictorRef
		40: SpeedFactor
		41: BoosterSpeedFactor
		42: AimSpeedFactor
		43: Deployed
}

disabled rule("============= Meka Modes ================")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Stats : Wrecking ball")
{
	event
	{
		Ongoing - Each Player;
		All;
		Wrecking Ball;
	}

	actions
	{
		Event Player.SpeedFactor = 10;
		Event Player.BoosterSpeedFactor = 130;
		Event Player.AimSpeedFactor = 0;
		Create Dummy Bot(Hero(Bastion), Team Of(Event Player), Slot Of(Event Player) + 3, Eye Position(Event Player) + Vector(0, 0, 0),
			Facing Direction Of(Event Player));
	}
}

rule("Stats : Pharah")
{
	event
	{
		Ongoing - Each Player;
		All;
		Pharah;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == False;
	}

	actions
	{
		Event Player.SpeedFactor = 30;
		Event Player.BoosterSpeedFactor = 100;
		Event Player.AimSpeedFactor = 10;
		Create Dummy Bot(Hero(Pharah), Team Of(Event Player), Slot Of(Event Player) + 3, Eye Position(Event Player) + Vector(0, 0, 0),
			Facing Direction Of(Event Player));
	}
}

rule("Stats : DVA")
{
	event
	{
		Ongoing - Each Player;
		All;
		D.Va;
	}

	actions
	{
		Event Player.SpeedFactor = 30;
		Event Player.BoosterSpeedFactor = 100;
		Event Player.AimSpeedFactor = 10;
		Create Dummy Bot(Hero(Pharah), Team Of(Event Player), Slot Of(Event Player) + 3, Eye Position(Event Player) + Vector(0, 0, 0),
			Facing Direction Of(Event Player));
	}
}

rule("Stats : Echo")
{
	event
	{
		Ongoing - Each Player;
		All;
		Echo;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == False;
	}

	actions
	{
		Event Player.SpeedFactor = 60;
		Event Player.BoosterSpeedFactor = 300;
		Event Player.AimSpeedFactor = 4;
		Create Dummy Bot(Hero(Echo), Team Of(Event Player), Slot Of(Event Player) + 3, Eye Position(Event Player) + Vector(0, 0, 0),
			Facing Direction Of(Event Player));
	}
}

rule("Stats : Sigma")
{
	event
	{
		Ongoing - Each Player;
		All;
		Sigma;
	}

	actions
	{
		Event Player.SpeedFactor = 30;
		Event Player.BoosterSpeedFactor = 120;
		Event Player.AimSpeedFactor = 6;
		Create Dummy Bot(Hero(Moira), Team Of(Event Player), Slot Of(Event Player) + 3, Eye Position(Event Player) + Vector(0, 0, 0),
			Facing Direction Of(Event Player));
	}
}

rule("Stats : Rein")
{
	event
	{
		Ongoing - Each Player;
		All;
		Reinhardt;
	}

	actions
	{
		Event Player.SpeedFactor = 60;
		Event Player.BoosterSpeedFactor = 100;
		Event Player.AimSpeedFactor = 10;
		Create Dummy Bot(Hero(Genji), Team Of(Event Player), Slot Of(Event Player) + 3, Eye Position(Event Player) + Vector(0, 0, 0),
			Facing Direction Of(Event Player));
	}
}

rule("TUTORIAL BUILD")
{
	event
	{
		Ongoing - Global;
	}

	actions
	{
		Create Effect(All Players(All Teams), Ring, Color(Green), Vector(198.560, 9.100, 213.560), Global.X,
			Visible To Position and Radius);
		Create Effect(All Players(All Teams), Sparkles, Color(Red), Vector(204.630, 9.100, 207.970), Global.X,
			Visible To Position and Radius);
		Create Effect(All Players(All Teams), Good Aura, Color(Yellow), Vector(210.280, 9.100, 205.290), Global.X,
			Visible To Position and Radius);
		Create Effect(All Players(All Teams), Bad Aura, Color(Blue), Vector(216.520, 9.100, 207.500), Global.X,
			Visible To Position and Radius);
		Create In-World Text(All Players(All Teams), String("{0} {1} {2}", Hero Icon String(Hero(Reinhardt)), Custom String("CN : D.MON")),
			Vector(203.680, 12, 207.290), 2, Clip Against Surfaces, Visible To Position and String, Color(Red), Default Visibility);
		Create In-World Text(All Players(All Teams), String("{0} {1} {2}", Hero Icon String(Hero(Reinhardt)), Custom String("CN : D.MON")),
			Vector(203.680, 11, 207.290), 1, Clip Against Surfaces, Visible To Position and String, Color(White), Default Visibility);
		Create In-World Text(All Players(All Teams), String("{0} {1} {2}", Hero Icon String(Hero(Wrecking Ball)), Custom String(
			"CN : CASINO")), Vector(200.650, 12, 213.650), 2, Clip Against Surfaces, Visible To and String, Color(White),
			Default Visibility);
		Create In-World Text(All Players(All Teams), String("{0} {1} {2}", Hero Icon String(Hero(Sigma)), Custom String("CN : KING")),
			Vector(210.380, 12, 204.160), 2, Clip Against Surfaces, Visible To Position and String, Color(White), Default Visibility);
		Create In-World Text(All Players(All Teams), String("{0} {1} {2}", Hero Icon String(Hero(D.Va)), Custom String("CN : OVERLORD")),
			Vector(217.270, 12, 206.540), 2, Clip Against Surfaces, Visible To Position and String, Color(White), Default Visibility);
	}
}

disabled rule("Shoot : Adjust rate of fire Pharah")
{
	event
	{
		Ongoing - Each Player;
		All;
		Pharah;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Primary Fire)) == True;
		disabled Hero Of(Event Player.Child) == Hero(Pharah);
	}

	actions
	{
		disabled Clear Status(Event Player, Stunned);
		disabled Press Button(Event Player.Child, Button(Primary Fire));
		disabled Wait(0.500, Ignore Condition);
		Set Status(Event Player, Null, Stunned, 0.100);
		Loop If Condition Is True;
	}
}

disabled rule("CodeSnippet")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Interact)) == True;
	}

	actions
	{
		Press Button(Event Player.Child, Button(Ability 2));
		Wait(0.016, Ignore Condition);
		Press Button(Event Player.Child, Button(Secondary Fire));
		Wait(0.016, Ignore Condition);
		disabled Set Status(Event Player.Child, Null, Knocked Down, 0.001);
		disabled Set Ultimate Charge(Players In Slot(1, All Teams), 100);
		disabled Press Button(Players In Slot(1, All Teams), Button(Ultimate));
		Wait(0.016, Ignore Condition);
		disabled Clear Status(Players In Slot(1, All Teams), Knocked Down);
		Loop If Condition Is True;
	}
}

disabled rule("============================ Special Conditions ==================================")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Ultimate : Pharah")
{
	event
	{
		Ongoing - Each Player;
		All;
		Pharah;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == False;
		Is Using Ultimate(Event Player) == True;
	}

	actions
	{
		Set Ultimate Ability Enabled(Event Player, False);
		Set Status(Event Player, Null, Hacked, 0.100);
		Wait(0.016, Ignore Condition);
		Clear Status(Event Player, Hacked);
		Set Ultimate Charge(Event Player, 0);
		Press Button(Event Player.Child, Button(Ultimate));
		Set Ultimate Ability Enabled(Event Player, True);
	}
}

rule("Bastion Booster Check")
{
	event
	{
		Ongoing - Each Player;
		All;
		Wrecking Ball;
	}

	conditions
	{
		Is Using Ability 1(Event Player) == True;
		Event Player.Child.Deployed == True;
	}

	actions
	{
		Press Button(Event Player.Child, Button(Ability 1));
		Wait(0.500, Ignore Condition);
		Event Player.Child.Deployed = False;
		Set Ammo(Event Player, 0, 60);
	}
}

rule("Bastion On / Off")
{
	event
	{
		Ongoing - Each Player;
		All;
		Wrecking Ball;
	}

	conditions
	{
		Is Using Ability 1(Event Player) == False;
		Event Player.Child.Deployed == False;
	}

	actions
	{
		Press Button(Event Player.Child, Button(Ability 1));
		Wait(1, Ignore Condition);
		Event Player.Child.Deployed = True;
	}
}

rule("Hack Slow Down")
{
	event
	{
		Player Dealt Damage;
		All;
		Moira;
	}

	conditions
	{
		Is Using Ultimate(Event Player) == True;
	}

	actions
	{
		Set Status(Victim, Null, Hacked, 0.200);
	}
}

rule("DEBUG : Set up")
{
	event
	{
		Ongoing - Each Player;
		All;
		Slot 0;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Interact)) == True;
		Is Button Held(Event Player, Button(Crouch)) == True;
	}

	actions
	{
		disabled Create Dummy Bot(Hero(Moira), Team 1, 1, Eye Position(Players In Slot(0, All Teams)) + Vector(0, 0, 0), Facing Direction Of(
			Event Player));
		disabled Create HUD Text(All Players(All Teams), Position Of(Players In Slot(0, All Teams)), Null, Position Of(Players In Slot(6,
			All Teams)), Left, 0, Color(White), Color(White), Color(White), Visible To and String, Default Visibility);
		Teleport(Event Player, Vector(215, 52, 235));
		disabled Create In-World Text(Players In Slot(0, All Teams), Custom String("", Health(Event Player)), Eye Position(Event Player.Target), 1,
			Do Not Clip, Visible To Position and String, Color(White), Default Visibility);
		disabled Create In-World Text(All Players(All Teams), String("{0} {1}", Hero Icon String(Hero Of(Players In Slot(7, Team 1))),
			Players In Slot(7, Team 1)), Position Of(Players In Slot(7, Team 1)), 1, Do Not Clip, Visible To Position and String, Color(
			White), Default Visibility);
		disabled Create Icon(All Players(All Teams), Event Player.Target, X, Visible To and Position, Color(Aqua), True);
		Wait(0.250, Ignore Condition);
		Create HUD Text(Players In Slot(0, All Teams), String("{0}: {1}", Custom String("Target", Players In Slot(0, All Teams).Target)),
			Null, Null, Left, 0, Color(White), Color(White), Color(White), Visible To and String, Default Visibility);
		Create Dummy Bot(Hero(Reinhardt), Team 2, 0, Vector(215, 60.300, 232), Vector(0, 0, 0));
		disabled Create Dummy Bot(Hero(Wrecking Ball), Team 2, 5, Vector(215, 52.300, 232), Vector(0, 0, 0));
		disabled Create Dummy Bot(Hero(Sigma), Team 2, 3, Vector(215, 68.300, 232), Vector(0, 0, 0));
		disabled Create Dummy Bot(Hero(D.Va), Team 2, 4, Vector(215, 76.300, 232), Vector(0, 0, 0));
	}
}

rule("Ultimate (Sigma)")
{
	event
	{
		Ongoing - Each Player;
		All;
		Sigma;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Ultimate)) == True;
		Is Dummy Bot(Event Player) != True;
	}

	actions
	{
		Set Ultimate Charge(Event Player.Child, 100);
		Press Button(Event Player.Child, Button(Ultimate));
		Event Player.SpeedFactor = 0;
		Event Player.BoosterSpeedFactor = 0;
		Event Player.AimSpeedFactor = 0;
		Wait(6, Ignore Condition);
		Event Player.SpeedFactor = 40;
		Event Player.BoosterSpeedFactor = 80;
		Event Player.AimSpeedFactor = 20;
		Set Status(Event Player.Child, Null, Hacked, 0.100);
	}
}

rule("Ultimate")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Ultimate)) == True;
		Is Dummy Bot(Event Player) != True;
		Hero Of(Event Player) == Hero(Sigma);
	}

	actions
	{
		Set Ultimate Charge(Event Player.Child, 100);
		Press Button(Event Player.Child, Button(Ultimate));
	}
}

disabled rule("FlyMode Special Type")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Jump)) == True;
		Event Player.GunnerMode != True;
		Hero Of(Event Player) == Hero(Pharah);
	}

	actions
	{
		disabled Start Accelerating(Event Player, Forward, 100, 400, To Player, None);
		Apply Impulse(Event Player, Left, 40 * Event Player.SpeedFactor, To Player, Cancel Contrary Motion);
		disabled Skip If(Y Component Of(Position Of(Event Player)) <= -7 && Y Component Of(Facing Direction Of(Event Player)) <= 0, 3);
		disabled Disallow Button(Event Player, Button(Secondary Fire));
		disabled Wait(1, Ignore Condition);
		disabled Apply Impulse(All Players(Team 1), Vector(X Component Of(Facing Direction Of(Event Player)), 0, Z Component Of(Facing Direction Of(
			Event Player))), 100, To World, Cancel Contrary Motion);
		Wait(0.064, Ignore Condition);
		disabled Apply Impulse(Players In Slot(1, All Teams), Facing Direction Of(Event Player), 100, To World, Cancel Contrary Motion);
		Loop If Condition Is True;
		disabled Stop Accelerating(Event Player);
	}
}

rule("FlyMode")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Jump)) == True;
		Event Player.GunnerMode != True;
		Has Status(Event Player, Hacked) != True;
	}

	actions
	{
		Apply Impulse(Event Player, Facing Direction Of(Event Player), Event Player.SpeedFactor, To World, Cancel Contrary Motion);
		disabled Start Accelerating(Event Player, Forward, 100, 400, To Player, None);
		disabled Apply Impulse(Event Player, Facing Direction Of(Event Player), 40 * Event Player.SpeedFactor, To Player, Cancel Contrary Motion);
		disabled Skip If(Y Component Of(Position Of(Event Player)) <= -7 && Y Component Of(Facing Direction Of(Event Player)) <= 0, 3);
		disabled Disallow Button(Event Player, Button(Secondary Fire));
		disabled Wait(1, Ignore Condition);
		disabled Apply Impulse(All Players(Team 1), Vector(X Component Of(Facing Direction Of(Event Player)), 0, Z Component Of(Facing Direction Of(
			Event Player))), 100, To World, Cancel Contrary Motion);
		Wait(0.128, Ignore Condition);
		disabled Apply Impulse(Players In Slot(1, All Teams), Facing Direction Of(Event Player), 100, To World, Cancel Contrary Motion);
		Loop If Condition Is True;
		disabled Stop Accelerating(Event Player);
	}
}

rule("BoosterMode")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Using Ability 1(Event Player) == True;
		disabled Is Button Held(Event Player, Button(Ability 1)) == True;
		Is Dummy Bot(Event Player) == False;
		disabled Hero Of(Event Player) != Hero(Reinhardt);
		Has Status(Event Player, Hacked) != True;
	}

	actions
	{
		Skip If(Has Status(Event Player, Hacked), 1);
		Apply Impulse(Event Player, Facing Direction Of(Event Player), Event Player.BoosterSpeedFactor, To World, Cancel Contrary Motion);
		Event Player.LocationPrediction = Eye Position(Event Player) + 1 * Velocity Of(Event Player);
		Skip If(Y Component Of(Position Of(Event Player)) <= -7 && Y Component Of(Facing Direction Of(Event Player)) <= 0, 1);
		Apply Impulse(All Players(Team 1), Vector(X Component Of(Facing Direction Of(Event Player)), 0, Z Component Of(Facing Direction Of(
			Event Player))), Event Player.BoosterSpeedFactor, To World, Cancel Contrary Motion);
		Wait(0.064, Ignore Condition);
		Loop If Condition Is True;
	}
}

rule("Melee GunnerMode")
{
	event
	{
		Ongoing - Each Player;
		All;
		Reinhardt;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Secondary Fire)) == True;
		Is Dummy Bot(Event Player) == False;
	}

	actions
	{
		Event Player.Target = Closest Player To(Eye Position(Event Player), Opposite Team Of(Team Of(Event Player)));
		Event Player.Child.Target = Event Player.Target;
		Event Player.GunnerMode = True;
		Start Facing(Event Player, Direction Towards(Eye Position(Event Player), Eye Position(Event Player.Target)), 1200, To World,
			Direction and Turn Rate);
		Wait(0.016, Ignore Condition);
		disabled Skip If(Is Button Held(Event Player, Button(Primary Fire)), 3);
		Skip If(Throttle Of(Event Player) == Vector(0, 0, 0), 1);
		Apply Impulse(Event Player, Vector(X Component Of(Throttle Of(Event Player)), Z Component Of(Throttle Of(Event Player)), 1),
			3 * Event Player.AimSpeedFactor, To Player, Cancel Contrary Motion);
		Loop If Condition Is True;
		Stop Facing(Event Player);
		Event Player.GunnerMode = False;
		Event Player.Target = Null;
		Event Player.Child.Target = Null;
	}
}

rule("GunnerMode")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Secondary Fire)) == True;
		Is Dummy Bot(Event Player) == False;
		Hero Of(Event Player) != Hero(Reinhardt);
		Has Status(Event Player, Hacked) != True;
	}

	actions
	{
		disabled Event Player.Target = Filtered Array(All Players(All Teams), Has Status(Current Array Element, Phased Out) == False);
		"Skip if currently has a target"
		Skip If(Event Player.Target != Null, 3);
		"Closest target of opposite team if not Dead, phased out(The bots) "
		Event Player.Target = Filtered Array(Filtered Array(All Players(Opposite Team Of(Team Of(Event Player))), Is Dead(Event Player)
			== False), Has Status(Current Array Element, Phased Out) == False);
		Event Player.Child.Target = Event Player.Target;
		Event Player.GunnerMode = True;
		Start Facing(Event Player, Direction Towards(Eye Position(Event Player), Eye Position(Event Player.Target)), 1200, To World,
			Direction and Turn Rate);
		Wait(0.016, Ignore Condition);
		Skip If(Throttle Of(Event Player) == Vector(0, 0, 0), 1);
		Apply Impulse(Event Player, Vector(X Component Of(Throttle Of(Event Player)), Z Component Of(Throttle Of(Event Player)), 1),
			Event Player.AimSpeedFactor, To Player, Cancel Contrary Motion);
		Loop If Condition Is True;
		Stop Facing(Event Player);
		Event Player.GunnerMode = False;
		Event Player.Target = Null;
		Event Player.Child.Target = Null;
	}
}

rule("GunnerMode : Show Predictor")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Alive(Event Player) == True;
		Is Dummy Bot(Event Player) == True;
	}

	actions
	{
		Create Effect(All Players(All Teams), Sphere, Color(Green), Event Player.LocationPrediction, 2, Visible To Position and Radius);
		Event Player.PredictorRef = Last Created Entity;
		Wait(1, Ignore Condition);
	}
}

disabled rule("============= Weapons Code ==============")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Setup : Genji")
{
	event
	{
		Ongoing - Each Player;
		All;
		Genji;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == True;
		Event Player.Parent == Null;
	}

	actions
	{
		Set Status(Event Player, Null, Phased Out, 9999);
		Event Player.A = Players In Slot(0, All Teams);
		disabled Set Invisible(Event Player, All);
		disabled Start Facing(Event Player, Direction Towards(Event Player, Position Of(All Players(Team 2)[0].LocationPrediction)), 10000,
			To World, Direction and Turn Rate);
		disabled Start Facing(Event Player, Direction Towards(Event Player, Vector(0, -1, 0) + All Players(Team 2)[0].LocationPrediction), 10000,
			To World, Direction and Turn Rate);
		Event Player.Parent = Closest Player To(Event Player, Team Of(Event Player));
		Event Player.Parent.Child = Event Player;
		Event Player.ProjectileSpeed = 70;
		disabled Set Invisible(Event Player, All);
		Set Ultimate Charge(Event Player, 100);
		Wait(1, Ignore Condition);
		Press Button(Event Player, Button(Ultimate));
	}
}

rule("Setup : Moira")
{
	event
	{
		Ongoing - Each Player;
		All;
		Moira;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == True;
		Event Player.Parent == Null;
	}

	actions
	{
		Set Status(Event Player, Null, Phased Out, 9999);
		Event Player.Parent = Closest Player To(Event Player, Team Of(Event Player));
		Event Player.A = Players In Slot(0, All Teams);
		disabled Set Invisible(Event Player, All);
		disabled Start Facing(Event Player, Direction Towards(Event Player, Position Of(All Players(Team 2)[0].LocationPrediction)), 10000,
			To World, Direction and Turn Rate);
		disabled Start Facing(Event Player, Direction Towards(Event Player, Vector(0, -1, 0) + All Players(Team 2)[0].LocationPrediction), 10000,
			To World, Direction and Turn Rate);
		Event Player.Parent.Child = Event Player;
		Event Player.ProjectileSpeed = 70;
		disabled Set Invisible(Event Player, All);
		disabled Press Button(Event Player, Button(Ultimate));
		Start Facing(Event Player, Facing Direction Of(Event Player.Parent), 10000, To World, Direction and Turn Rate);
	}
}

rule("Setup : Echo")
{
	event
	{
		Ongoing - Each Player;
		All;
		Echo;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == True;
		Event Player.Parent == Null;
	}

	actions
	{
		Set Status(Event Player, Null, Phased Out, 9999);
		Event Player.A = Players In Slot(0, All Teams);
		disabled Set Invisible(Event Player, All);
		disabled Start Facing(Event Player, Direction Towards(Event Player, Position Of(All Players(Team 2)[0].LocationPrediction)), 10000,
			To World, Direction and Turn Rate);
		disabled Start Facing(Event Player, Direction Towards(Event Player, Vector(0, -1, 0) + All Players(Team 2)[0].LocationPrediction), 10000,
			To World, Direction and Turn Rate);
		Event Player.Parent = Closest Player To(Event Player, Team Of(Event Player));
		Event Player.Parent.Child = Event Player;
		Event Player.ProjectileSpeed = 70;
		disabled Set Invisible(Event Player, All);
		Set Ultimate Charge(Event Player, 100);
		Wait(1, Ignore Condition);
		Press Button(Event Player, Button(Ultimate));
	}
}

rule("Setup : Bastion")
{
	event
	{
		Ongoing - Each Player;
		All;
		Bastion;
	}

	conditions
	{
		Event Player.Parent == Null;
		Is Dummy Bot(Event Player) == True;
	}

	actions
	{
		disabled Event Player.Parent = Closest Player To(Event Player, Team Of(Event Player));
		disabled Start Facing(Event Player, Facing Direction Of(Event Player.Parent), 10000, To World, Direction and Turn Rate);
		disabled Set Status(Event Player, Null, Phased Out, 9999);
		disabled Event Player.A = Players In Slot(0, All Teams);
		disabled Set Invisible(Event Player, All);
		Set Status(Event Player, Null, Phased Out, 9999);
		Press Button(Event Player, Button(Ability 1));
		Event Player.Parent = Closest Player To(Event Player, Team Of(Event Player));
		Event Player.Parent.Child = Event Player;
		Event Player.ProjectileSpeed = 70;
		disabled Set Invisible(Event Player, All);
		Start Facing(Event Player, Facing Direction Of(Event Player.Parent), 10000, To World, Direction and Turn Rate);
		Event Player.A = Event Player.Parent;
	}
}

rule("Setup : Pharah")
{
	event
	{
		Ongoing - Each Player;
		All;
		Pharah;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == True;
		Event Player.Parent == Null;
	}

	actions
	{
		Set Status(Event Player, Null, Phased Out, 9999);
		Event Player.A = Players In Slot(0, All Teams);
		disabled Set Invisible(Event Player, All);
		disabled Start Facing(Event Player, Direction Towards(Event Player, Position Of(All Players(Team 2)[0].LocationPrediction)), 10000,
			To World, Direction and Turn Rate);
		disabled Start Facing(Event Player, Direction Towards(Event Player, Vector(0, -1, 0) + All Players(Team 2)[0].LocationPrediction), 10000,
			To World, Direction and Turn Rate);
		Event Player.Parent = Closest Player To(Event Player, Team Of(Event Player));
		Event Player.Parent.Child = Event Player;
		Event Player.ProjectileSpeed = 70;
		Set Invisible(Event Player, All);
	}
}

rule("Prediction for Projectiles")
{
	event
	{
		Ongoing - Each Player;
		All;
		Pharah;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == True;
		Event Player.Target != Null;
		Is Button Held(Event Player.Parent, Button(Secondary Fire)) == True;
	}

	actions
	{
		disabled Skip If(Event Player.Target != Null, 1);
		disabled Event Player.Target = Event Player.Parent.Target;
		Start Facing(Event Player, Direction Towards(Eye Position(Event Player), Event Player.LocationPrediction), 10000, To World,
			Direction and Turn Rate);
		Event Player.Distance = Distance Between(Eye Position(Event Player), Eye Position(Event Player.Target) + Vector(0, 0, 0));
		Event Player.ProjectileAirTime = Event Player.Distance / Event Player.ProjectileSpeed;
		Event Player.LocationPrediction = Eye Position(Event Player.Target) + Vector(0, 0, 0) + Velocity Of(Event Player.Target)
			* Event Player.ProjectileAirTime;
		disabled Event Player.LocationPrediction = Eye Position(Event Player) + 1 * Velocity Of(Event Player);
		Wait(0.016, Ignore Condition);
		Loop If(Event Player.Target != Null);
		Event Player.Target = Null;
	}
}

rule("Set Gravity")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	actions
	{
		Set Gravity(Event Player, 0);
	}
}

rule("Stack bot - Thanks Squ1dward for the original code")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		All;
	}

	conditions
	{
		Event Player.Parent != Null;
		Is Dummy Bot(Event Player) == True;
	}

	actions
	{
		Attach Players(Event Player, Event Player.Parent, Eye Position(Event Player.Parent) + 0);
		disabled Apply Impulse(Event Player, Direction Towards(Position Of(Event Player), Position Of(Event Player) + Vector(Speed Of In Direction(
			Event Player, Left), Vertical Speed Of(Event Player), Speed Of In Direction(Event Player, Forward))), Speed Of(Event Player)
			* -0.800, To World, Incorporate Contrary Motion);
		disabled Apply Impulse(Event Player, Direction Towards(Event Player, Eye Position(Event Player.A) + Vector(0, Distance Between(Eye Position(
			Event Player), Position Of(Event Player)) * -1, 0)), Distance Between(Position Of(Event Player), Eye Position(Event Player.A)
			+ Vector(0, Distance Between(Eye Position(Event Player), Position Of(Event Player)) * -1, 0)) * 10, To World,
			Cancel Contrary Motion);
		disabled Skip If(Distance Between(Position Of(Event Player), Eye Position(Event Player.A) + Vector(0, Distance Between(Eye Position(
			Event Player), Position Of(Event Player)) * -1, 0)) < 2 || Is Alive(Event Player.A) != True, 3);
		disabled Event Player.C = Vertical Facing Angle Of(Event Player);
		disabled Teleport(Event Player, Vector(X Component Of(Position Of(Event Player.A)), Y Component Of(Eye Position(Event Player.A))
			+ Distance Between(Eye Position(Event Player), Position Of(Event Player)) * -1, Z Component Of(Position Of(Event Player.A))));
		disabled Set Facing(Event Player, Direction From Angles(Horizontal Facing Angle Of(Event Player), Event Player.C), To World);
		disabled Wait(0.016, Ignore Condition);
		disabled Loop If Condition Is True;
	}
}

rule("Shoot (Sigma/Moira)")
{
	event
	{
		Ongoing - Each Player;
		All;
		Sigma;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Primary Fire)) == True;
		Is Dummy Bot(Event Player) == False;
	}

	actions
	{
		Press Button(Event Player.Child, Button(Ability 2));
		Wait(0.100, Ignore Condition);
		Press Button(Event Player.Child, Button(Secondary Fire));
		Wait(0.700, Ignore Condition);
		Loop If Condition Is True;
	}
}

rule("Shoot(Reinhardt/Genji)")
{
	event
	{
		Ongoing - Each Player;
		All;
		Reinhardt;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Primary Fire)) == True;
		Is Dummy Bot(Event Player) == False;
	}

	actions
	{
		disabled Set Facing(Event Player, Direction Towards(Eye Position(Event Player), Eye Position(Event Player.Target)), To World);
		Wait(0.016, Ignore Condition);
		Press Button(Event Player.Child, Button(Ability 1));
		Wait(0.500, Ignore Condition);
		Press Button(Event Player.Child, Button(Primary Fire));
		Loop If Condition Is True;
	}
}

rule("Shoot")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Primary Fire)) == True;
		Is Dummy Bot(Event Player) == False;
		Hero Of(Event Player) != Hero(Sigma);
		Hero Of(Event Player) != Hero(Reinhardt);
	}

	actions
	{
		Start Holding Button(Event Player.Child, Button(Primary Fire));
	}
}

rule("Not shooting")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Primary Fire)) != True;
		Is Dummy Bot(Event Player) == False;
	}

	actions
	{
		Stop Holding Button(Event Player.Child, Button(Primary Fire));
	}
}

disabled rule("DEBUG : Target")
{
	event
	{
		Ongoing - Each Player;
		All;
		Roadhog;
	}

	actions
	{
		Teleport(Event Player, Vector(215, 52, 232));
	}
}

rule("SaveFromDeathbox")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Y Component Of(Position Of(Event Player)) < -7;
	}

	actions
	{
		Apply Impulse(Event Player, Up, 2, To World, Cancel Contrary Motion);
		Set Facing(Event Player, Vector(X Component Of(Facing Direction Of(Event Player)), 0.030, Z Component Of(Facing Direction Of(
			Event Player))), To World);
		Play Effect(All Players(All Teams), Ring Explosion, Color(White), Event Player, 1);
		Wait(0.016, Ignore Condition);
		Loop If Condition Is True;
	}
}

rule("Roof")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Y Component Of(Position Of(Event Player)) > 300;
	}

	actions
	{
		Apply Impulse(Event Player, Down, 25, To World, Cancel Contrary Motion);
		disabled Set Facing(Event Player, Vector(X Component Of(Facing Direction Of(Event Player)), 0.030, Z Component Of(Facing Direction Of(
			Event Player))), To World);
		disabled Play Effect(All Players(All Teams), Ring Explosion, Color(White), Event Player, 1);
		Wait(0.016, Ignore Condition);
		Loop If Condition Is True;
		Create HUD Text(All Players(All Teams), Custom String("Cieling"), Null, Null, Left, 0, Color(White), Color(White), Color(White),
			Visible To and String, Default Visibility);
	}
}

rule("WarnOfDeathbox")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Y Component Of(Event Player.LocationPrediction) < -7;
	}

	actions
	{
		Start Facing(Event Player, Vector(X Component Of(Facing Direction Of(Event Player)), 0, Z Component Of(Facing Direction Of(
			Event Player))), 100, To World, Direction and Turn Rate);
		disabled Apply Impulse(Event Player, Up, 5, To World, Incorporate Contrary Motion);
		Wait(0.016, Ignore Condition);
		Loop If Condition Is True;
		Stop Facing(Event Player);
	}
}

rule("If dies below level")
{
	event
	{
		Player Died;
		All;
		All;
	}

	conditions
	{
		Attacker == Null;
	}

	actions
	{
		Teleport(Event Player, Vector(X Component Of(Position Of(Event Player)), -7, Z Component Of(Position Of(Event Player))));
		Respawn(Event Player);
	}
}

disabled rule("Rule 59")
{
	event
	{
		Ongoing - Each Player;
		All;
		Bastion;
	}

	actions
	{
		Event Player.C = Vertical Facing Angle Of(Event Player);
		Teleport(Event Player, Eye Position(Event Player.A));
		Set Facing(Event Player, Direction From Angles(Horizontal Facing Angle Of(Event Player), Event Player.C), To World);
		Wait(0.016, Ignore Condition);
		Loop;
	}
}

rule("Camera Distance Factor == [Default = 1]")
{
	event
	{
		Ongoing - Global;
	}

	actions
	{
		Global.C = 1;
	}
}

disabled rule("TELEPORT")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Interact)) == True;
		Is Button Held(Event Player, Button(Crouch)) == False;
		Is Button Held(Event Player, Button(Secondary Fire)) == False;
		Event Player.M != 10;
		Global.P == True;
	}

	actions
	{
		Skip If(Event Player.O != Null, 4);
		Create Effect(Event Player, Sphere, Color(Yellow), World Vector Of(Vector(0, Sine From Degrees(Vertical Facing Angle Of(
			Event Player)) * Global.TeleportRangeFactor * -9 + 1.500, Cosine From Degrees(Vertical Facing Angle Of(Event Player))
			* Global.TeleportRangeFactor * 9), Event Player, Rotation And Translation), 0.120, Visible To Position and Radius);
		Event Player.O[0] = Last Created Entity;
		Create Effect(Event Player, Ring, Color(Yellow), Ray Cast Hit Position(World Vector Of(Vector(0, Sine From Degrees(
			Vertical Facing Angle Of(Event Player)) * Global.TeleportRangeFactor * -9 + 1.500, Cosine From Degrees(
			Vertical Facing Angle Of(Event Player)) * Global.TeleportRangeFactor * 9), Event Player, Rotation And Translation),
			World Vector Of(Vector(0, -1000, Cosine From Degrees(Vertical Facing Angle Of(Event Player)) * Global.TeleportRangeFactor * 9),
			Event Player, Rotation And Translation), Null, All Players(All Teams), False), 0.200, Visible To Position and Radius);
		Event Player.O[1] = Last Created Entity;
		Wait(0.016, Ignore Condition);
		Loop If(Is Button Held(Event Player, Button(Interact)));
		Event Player.V = Vector(0, Global.TeleportRangeFactor * -9 * Sine From Degrees(Vertical Facing Angle Of(Event Player)),
			Cosine From Degrees(Vertical Facing Angle Of(Event Player)) * Global.TeleportRangeFactor * 9);
		Skip If(Is Button Held(Event Player, Button(Secondary Fire)) == True, 2);
		Teleport(Event Player, World Vector Of(Event Player.V, Event Player, Rotation And Translation));
		Set Facing(Event Player, World Vector Of(Event Player.V, Event Player, Rotation), To World);
		Destroy Effect(Event Player.O[0]);
		Destroy Effect(Event Player.O[1]);
		Event Player.O = Null;
	}
}

disabled rule("Skip assembly phase")
{
	event
	{
		Ongoing - Global;
	}

	conditions
	{
		Is Assembling Heroes == True;
	}

	actions
	{
		Set Match Time(1);
	}
}

rule("TP Mode > Teleport to + toggle tp")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Event Player.M == 3;
		Is Button Held(Event Player, Button(Primary Fire)) == True;
	}

	actions
	{
		Skip If(Is Button Held(Event Player, Button(Crouch)) == True, 1);
		Teleport(Event Player, Player Closest To Reticle(Event Player, All Teams));
		Skip If(Is Button Held(Event Player, Button(Crouch)) == False, 6);
		Skip If(Event Player.T == False, 2);
		Event Player.T = False;
		Abort;
		Skip If(Event Player.T == True, 2);
		Event Player.T = True;
		Abort;
	}
}

rule("TP Mode > Bring here + Bring everyonE here")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Event Player.M == 3;
		Is Button Held(Event Player, Button(Secondary Fire)) == True;
	}

	actions
	{
		Skip If(Is Button Held(Event Player, Button(Crouch)) == True, 1);
		Teleport(Filtered Array(Player Closest To Reticle(Event Player, All Teams), Current Array Element.T == True), Event Player);
		Skip If(Is Button Held(Event Player, Button(Crouch)) == False, 1);
		Teleport(Filtered Array(All Players(All Teams), Current Array Element.T == True), Event Player);
	}
}

rule("O==========HUD ELEMENTS==========O")
{
	event
	{
		Ongoing - Global;
	}

	actions
	{
		Global.A = True;
	}
}

rule("Mod See players through walls while crouching - HUD")
{
	event
	{
		Ongoing - Global;
	}

	conditions
	{
		Global.A == True;
	}

	actions
	{
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(0, Team 1))), Players In Slot(0, Team 1)), Position Of(Players In Slot(0, Team 1)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(1, Team 1))), Players In Slot(1, Team 1)), Position Of(Players In Slot(1, Team 1)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(2, Team 1))), Players In Slot(2, Team 1)), Position Of(Players In Slot(2, Team 1)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(3, Team 1))), Players In Slot(3, Team 1)), Position Of(Players In Slot(3, Team 1)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(4, Team 1))), Players In Slot(4, Team 1)), Position Of(Players In Slot(4, Team 1)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(5, Team 1))), Players In Slot(5, Team 1)), Position Of(Players In Slot(5, Team 1)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(0, Team 2))), Players In Slot(0, Team 2)), Position Of(Players In Slot(0, Team 2)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(1, Team 2))), Players In Slot(1, Team 2)), Position Of(Players In Slot(1, Team 2)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(2, Team 2))), Players In Slot(2, Team 2)), Position Of(Players In Slot(2, Team 2)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(3, Team 2))), Players In Slot(3, Team 2)), Position Of(Players In Slot(3, Team 2)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(4, Team 2))), Players In Slot(4, Team 2)), Position Of(Players In Slot(4, Team 2)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
		Wait(0.100, Ignore Condition);
		Create In-World Text(Filtered Array(All Players(All Teams), Is Button Held(Current Array Element, Button(Crouch))
			== True && Current Array Element.D >= 1 && Current Array Element.M != 10), String("{0} {1}", Hero Icon String(Hero Of(
			Players In Slot(5, Team 2))), Players In Slot(5, Team 2)), Position Of(Players In Slot(5, Team 2)), 1, Do Not Clip,
			Visible To Position and String, Color(White), Default Visibility);
	}
}

rule("O==========CAMERA==========O")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Camera MODE 2 - FAR")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	actions
	{
		Start Camera(Event Player, Ray Cast Hit Position(Eye Position(Event Player), Eye Position(Event Player) + World Vector Of(Vector(
			-0.400, 0, 0.300), Event Player, Rotation) + Facing Direction Of(Event Player) * -6 * Global.C, Null, Event Player, False),
			Event Player + Facing Direction Of(Event Player) * 1000, 40);
	}
}

rule("Set Variables")
{
	event
	{
		Ongoing - Global;
	}

	conditions
	{
		Global.A == True;
	}
}

rule("Zen Autofire")
{
	event
	{
		Ongoing - Each Player;
		All;
		Zenyatta;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Primary Fire)) == True;
	}

	actions
	{
		Set Status(Event Player, Null, Knocked Down, 0.001);
		Wait(0.050, Ignore Condition);
		Press Button(Event Player, Button(Primary Fire));
		Clear Status(Event Player, Knocked Down);
		Wait(0.050, Ignore Condition);
		Loop If Condition Is True;
	}
}

disabled rule("create in world")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	actions
	{
		Create In-World Text(All Players(All Teams), String("-> {0}", Position Of(Event Player)), Event Player, 2, Clip Against Surfaces,
			Visible To Position and String, Color(White), Default Visibility);
	}
}

rule("teleport")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Interact)) == True;
	}
}

rule("TELEPORT")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Interact)) == True;
		Is Button Held(Event Player, Button(Crouch)) == False;
		Is Button Held(Event Player, Button(Secondary Fire)) == False;
	}

	actions
	{
		Skip If(Event Player.O != Null, 4);
		Create Effect(Event Player, Sphere, Color(Yellow), World Vector Of(Vector(0, Sine From Degrees(Vertical Facing Angle Of(
			Event Player)) * -9 + 1.500, Cosine From Degrees(Vertical Facing Angle Of(Event Player)) * 9), Event Player,
			Rotation And Translation), 0.120, Visible To Position and Radius);
		Event Player.O[0] = Last Created Entity;
		Create Effect(Event Player, Ring, Color(Yellow), Ray Cast Hit Position(World Vector Of(Vector(0, Sine From Degrees(
			Vertical Facing Angle Of(Event Player)) * -9, Cosine From Degrees(Vertical Facing Angle Of(Event Player)) * 9), Event Player,
			Rotation And Translation), World Vector Of(Vector(0, -1000, Cosine From Degrees(Vertical Facing Angle Of(Event Player)) * 9),
			Event Player, Rotation And Translation), Null, All Players(All Teams), False), 0.200, Visible To Position and Radius);
		Event Player.O[1] = Last Created Entity;
		Wait(0.016, Ignore Condition);
		Loop If(Is Button Held(Event Player, Button(Interact)));
		Event Player.V = Vector(0, -9 * Sine From Degrees(Vertical Facing Angle Of(Event Player)), Cosine From Degrees(
			Vertical Facing Angle Of(Event Player)) * 9);
		Skip If(Is Button Held(Event Player, Button(Secondary Fire)) == True, 2);
		Teleport(Event Player, World Vector Of(Event Player.V, Event Player, Rotation And Translation));
		Set Facing(Event Player, World Vector Of(Event Player.V, Event Player, Rotation), To World);
		Destroy Effect(Event Player.O[0]);
		Destroy Effect(Event Player.O[1]);
		Event Player.O = Null;
	}
}

rule("NewPrediction")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is Dummy Bot(Event Player) != True;
	}

	actions
	{
		Wait(0.064, Ignore Condition);
		Event Player.LocationPrediction = Eye Position(Event Player) + 1 * Velocity Of(Event Player);
		Loop;
	}
}

disabled rule("In Spawnroom")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Is In Spawn Room(Event Player) == True;
	}

	actions
	{
		Start Forcing Player To Be Hero(Event Player, Hero(D.Va));
		Teleport(Event Player, Vector(210.370, 9.100, 213.250));
	}
}

rule("Pulse X")
{
	event
	{
		Ongoing - Global;
	}

	actions
	{
		Global.X = 0;
		Chase Global Variable Over Time(X, 3, 6, Destination and Duration);
		Wait(10, Ignore Condition);
		Chase Global Variable Over Time(X, 0, 6, Destination and Duration);
		Wait(10, Ignore Condition);
		Loop;
	}
}

disabled rule("Rein Switch Dive")
{
	event
	{
		Ongoing - Each Player;
		All;
		Reinhardt;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Primary Fire)) == True;
		Is Button Held(Event Player, Button(Secondary Fire)) == True;
	}

	actions
	{
		Start Holding Button(Event Player, Button(Secondary Fire));
		disabled Disallow Button(Event Player, Button(Secondary Fire));
		Press Button(Event Player, Button(Ability 1));
		Apply Impulse(Event Player, Facing Direction Of(Event Player), 50, To World, Cancel Contrary Motion);
		Wait(0.050, Ignore Condition);
		Set Status(Event Player, Null, Knocked Down, 0.016);
		Start Holding Button(Event Player, Button(Primary Fire));
		Wait(0.300, Ignore Condition);
		Stop Holding Button(Event Player, Button(Primary Fire));
		disabled Loop If(Is Button Held(Event Player, Button(Primary Fire)));
		Apply Impulse(Event Player, Facing Direction Of(Event Player), 20, To World, Cancel Contrary Motion);
		disabled Allow Button(Event Player, Button(Secondary Fire));
		disabled Stop Holding Button(Event Player, Button(Secondary Fire));
		disabled Wait(0.560, Ignore Condition);
	}
}

rule("Rein")
{
	event
	{
		Ongoing - Each Player;
		All;
		Reinhardt;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Primary Fire)) == True;
	}

	actions
	{
		Apply Impulse(Event Player, Direction Towards(Position Of(Event Player), Position Of(Event Player.Target)),
			Event Player.SpeedFactor, To World, Cancel Contrary Motion);
		Wait(0.100, Ignore Condition);
		Loop If Condition Is True;
	}
}

rule("Hammond slam check")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Reinshift")
{
	event
	{
		Ongoing - Each Player;
		All;
		Reinhardt;
	}

	conditions
	{
		Is Button Held(Event Player, Button(Ability 1)) == True;
	}

	actions
	{
		Teleport(Event Player.Target, World Vector Of(Facing Direction Of(Event Player), Event Player, Rotation));
	}
}

rule("Grow Genji")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Debug : Location")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	actions
	{
		Create HUD Text(All Players(All Teams), Position Of(Event Player), Null, Null, Left, 0, Color(White), Color(White), Color(White),
			Visible To and String, Default Visibility);
	}
}

rule("Teleport high")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	conditions
	{
		Button(Interact) == True;
	}

	actions
	{
		Teleport(Event Player, Position Of(Event Player) + Vector(0, 400, 0));
	}
}