rule("Make First couple of rounds Harder")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		All;
	}

	conditions
	{
		Is Using Ultimate(Event Player) == True;
		Match Time < 360;
	}

	actions
	{
		Wait(8, Ignore Condition);
		Set Ultimate Charge(Event Player, 100);
		Press Button(Event Player, Button(Ultimate));
	}
}

rule("Damage Scalar Start")
{
	event
	{
		Ongoing - Global;
	}

	actions
	{
		Global.A = 160;
		Global.B = 70;
		Global.C = 250;
		Global.T = Random Value In Array(All Players(Team 1));
	}
}

rule("Damage Scalar : 6 minutes and back to normal")
{
	event
	{
		Ongoing - Global;
	}

	conditions
	{
		Is Game In Progress == True;
		Match Time < 360;
	}

	actions
	{
		Wait(60, Ignore Condition);
		Global.A -= 10;
		Global.B += 5;
		Loop If Condition Is True;
		Global.R = False;
	}
}

rule("Damage Scalar Initiate")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		All;
	}

	conditions
	{
		Has Spawned(Event Player) == True;
	}

	actions
	{
		Set Damage Dealt(Event Player, Global.A);
		Set Damage Received(Event Player, Global.B);
	}
}

rule("Least health on team")
{
	event
	{
		Player Took Damage;
		Team 1;
		All;
	}

	conditions
	{
		(Health(Event Player) < Health(Global.T)) == True;
	}

	actions
	{
		Global.T = Event Player;
	}
}

rule("Spawn Protection")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		All;
	}

	conditions
	{
		Has Spawned(Event Player) == True;
	}

	actions
	{
		Set Status(Event Player, Null, Invincible, 10);
		Set Status(Event Player, Null, Phased Out, 10);
	}
}

rule("Stop game auto ending")
{
	event
	{
		Ongoing - Global;
	}

	conditions
	{
		Match Time > 10;
		Global.R == False;
	}

	actions
	{
		Abort If Condition Is False;
		Create Dummy Bot(Hero(Reinhardt), Team 1, Global.R, Vector(89.100, 12.660, -63.670), Forward);
		Wait(0.250, Ignore Condition);
		Global.S += 1;
		Loop If Condition Is True;
	}
}

rule("Stop game auto ending part 2")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		Reinhardt;
	}

	conditions
	{
		Is Dummy Bot(Event Player) == True;
		Is Alive(Event Player) == True;
	}

	actions
	{
		Set Status(Event Player, Null, Phased Out, 10000);
		Set Status(Event Player, Null, Invincible, 10000);
		Create Effect(All Players(All Teams), Sparkles, Color(Yellow), Event Player, 1.500, Visible To Position and Radius);
		Start Facing(Event Player, Direction Towards(Event Player, Vector(88.300, 12, -67.700)), 100, To World, Direction and Turn Rate);
		Global.R = True;
		Event Player.K = True;
		Set Invisible(Event Player, All);
	}
}

rule("Half players dead Shatter")
{
	event
	{
		Ongoing - Each Player;
		Team 1;
		Reinhardt;
	}

	conditions
	{
		Number Of Dead Players(Team 1) > 3;
		Is Dummy Bot(Event Player) == True;
	}

	actions
	{
		Set Ultimate Charge(Event Player, 100);
		Press Button(Event Player, Button(Ultimate));
		Wait(15, Ignore Condition);
		Loop If Condition Is True;
	}
}

disabled rule("On Death Destory Effects")
{
	event
	{
		Player Died;
		Team 2;
		All;
	}

	actions
	{
		Destroy Effect(Event Player.Z[0]);
		Destroy Effect(Event Player.Z[1]);
		Destroy Effect(Event Player.Z[2]);
		Destroy Effect(Event Player.Z[3]);
	}
}

disabled rule("=========== Junk ===========")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Junk : AURA")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Junkrat;
	}

	conditions
	{
		Is Alive(Event Player) == True;
	}

	actions
	{
		Create Effect(All Players(All Teams), Sparkles, Color(Orange), Event Player, 1, Visible To Position and Radius);
	}
}

rule("Junk : Drop bomb randomly")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Junkrat;
	}

	conditions
	{
		Is Alive(Event Player) == True;
		Ultimate Charge Percent(Event Player) == 100;
	}

	actions
	{
		Play Effect(All Players(All Teams), Good Explosion, Color(Orange), Event Player, 1);
		Teleport(Event Player, Position Of(Random Value In Array(Filtered Array(All Players(Team 1), Current Array Element.K != True))));
		Global.K = Filtered Array(All Players(Team 1), Current Array Element.K != True);
		Wait(1, Ignore Condition);
		Start Facing(Event Player, Direction Towards(Event Player, Payload Position), Random Value In Array(All Players(Team 1)), To World,
			Direction and Turn Rate);
		Press Button(Event Player, Button(Ultimate));
		Create Icon(All Players(All Teams), Event Player, Warning, Visible To and Position, Color(Orange), True);
		Event Player.K = Last Created Entity;
		Wait(1.700, Ignore Condition);
		Play Effect(All Players(All Teams), Good Explosion, Color(Orange), Event Player, 1);
		Teleport(Event Player, Vector(84.750, 18.850, -105));
		Wait(2, Ignore Condition);
		Destroy Effect(Event Player.K);
		Press Button(Event Player, Button(Primary Fire));
	}
}

disabled rule("=========== Road ===========")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Road : Ultimate Pull")
{
	event
	{
		Player Dealt Damage;
		All;
		Roadhog;
	}

	conditions
	{
		Is Using Ultimate(Event Player) == True;
	}

	actions
	{
		Apply Impulse(Victim, Direction Towards(Victim, Event Player) + Vector(0, 0.100, 0), 7, To World, Incorporate Contrary Motion);
		Wait(0.200, Ignore Condition);
	}
}

rule("Road : Aura")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Roadhog;
	}

	conditions
	{
		Has Spawned(Event Player) == True;
	}

	actions
	{
		Create Effect(All Players(All Teams), Cloud, Color(Green), Event Player, 3, Visible To Position and Radius);
		Modify Player Variable(Event Player, Z, Append To Array, Last Text ID);
		Create Effect(All Players(All Teams), Ring, Color(Green), Event Player, 3, Visible To Position and Radius);
		Modify Player Variable(Event Player, Z, Append To Array, Last Text ID);
	}
}

rule("Road : AOE DMG")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Roadhog;
	}

	conditions
	{
		Is Alive(Event Player) == True;
	}

	actions
	{
		Event Player.R = Players Within Radius(Event Player, 5, Team 1, Off);
		Start Damage Over Time(Event Player.R[0], Event Player, 3, 20);
		Set Status(Event Player.R[0], Null, Burning, 5);
		Start Damage Over Time(Event Player.R[1], Event Player, 3, 20);
		Set Status(Event Player.R[1], Null, Burning, 5);
		Start Damage Over Time(Event Player.R[2], Event Player, 3, 20);
		Set Status(Event Player.R[2], Null, Burning, 5);
		Start Damage Over Time(Event Player.R[3], Event Player, 3, 20);
		Set Status(Event Player.R[3], Null, Burning, 5);
		Start Damage Over Time(Event Player.R[4], Event Player, 3, 20);
		Set Status(Event Player.R[4], Null, Burning, 5);
		Start Damage Over Time(Event Player.R[5], Event Player, 3, 20);
		Set Status(Event Player.R[5], Null, Burning, 5);
		Wait(1, Ignore Condition);
		Loop If Condition Is True;
	}
}

disabled rule("=========== Mercy ===========")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Mercy : AURA")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Mercy;
	}

	conditions
	{
		Is Alive(Event Player) == True;
	}

	actions
	{
		Create Effect(All Players(All Teams), Good Aura, Color(White), Event Player, 1, Visible To Position and Radius);
		Modify Player Variable(Event Player, Z, Append To Array, Last Created Entity);
		Start Facing(Event Player, Facing Direction Of(Closest Player To(Event Player, Team 1)), 100, To World, Direction and Turn Rate);
	}
}

disabled rule("=========== SYMMETRA ===========")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Symmetra : Aura and Zero G")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Symmetra;
	}

	conditions
	{
		Has Spawned(Event Player) == True;
	}

	actions
	{
		Create Effect(All Players(All Teams), Sparkles, Color(Red), Event Player, 1, Position and Radius);
		Set Gravity(Event Player, 0);
	}
}

rule("Symmetra : Auto Fire")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Symmetra;
	}

	conditions
	{
		Has Spawned(Event Player) == True;
		Is Using Ability 1(Event Player) == False;
	}

	actions
	{
		Press Button(Event Player, Button(Secondary Fire));
		Wait(0.100, Ignore Condition);
		Loop If Condition Is True;
	}
}

rule("Symmetra : Spawn turrets")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Symmetra;
	}

	conditions
	{
		Is Using Ability 1(Event Player) == False;
	}

	actions
	{
		Start Facing(Event Player, Direction Towards(Event Player, Position Of(Random Value In Array(Filtered Array(All Living Players(
			Team 1), Is Dummy Bot(Current Array Element) == False)))), 1000, To World, Direction and Turn Rate);
		Set Ability 1 Enabled(Event Player, True);
		Press Button(Event Player, Button(Ability 1));
		Wait(9, Ignore Condition);
		Set Ability 1 Enabled(Event Player, False);
		Loop If Condition Is True;
	}
}

rule("Symmetra : Fall on status")
{
	event
	{
		Player Took Damage;
		Team 2;
		Symmetra;
	}

	conditions
	{
		(Has Status(Event Player, Hacked) || Has Status(Event Player, Frozen) || Has Status(Event Player, Asleep) || Has Status(
			Event Player, Stunned)) == True;
	}

	actions
	{
		Set Gravity(Event Player, 100);
		Wait(3, Abort When False);
		Set Gravity(Event Player, 0);
		Apply Impulse(Event Player, Up, 4, To World, Incorporate Contrary Motion);
	}
}

rule("Symmetra : Center on stuck")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Symmetra;
	}

	conditions
	{
		Is Alive(Event Player) == True;
	}

	actions
	{
		Event Player.P = Event Player;
		Apply Impulse(Event Player, Vector Towards(Event Player, Vector(78, 20, -98)), 5, To World, Cancel Contrary Motion);
		Play Effect(All Players(All Teams), Good Explosion, Color(Red), Vector(78, 20, -98), 2);
		Wait(3, Ignore Condition);
		Loop If Condition Is True;
	}
}

disabled rule("=========== REAPER ===========")
{
	event
	{
		Ongoing - Global;
	}
}

rule("Reaper : Ult Jump")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Reaper;
	}

	conditions
	{
		Is Using Ultimate(Event Player) == True;
	}

	actions
	{
		Abort If(Is Using Ultimate(Event Player) == False);
		Event Player.A = Players Within Radius(Event Player, 5, Team 1, Off);
		Event Player.C = Remove From Array(Event Player.A, Event Player.B);
		Event Player.D = Count Of(Event Player.C);
		Wait(0.100, Ignore Condition);
		Loop If(Count Of(Event Player.C) == 0);
		Teleport(Event Player, Position Of(Event Player.C[0]));
		Wait(0.250, Ignore Condition);
		Play Effect(All Players(All Teams), Good Pickup Effect, Color(Purple), Event Player, 1);
		Set Status(Event Player.C[0], Null, Hacked, 5);
		Modify Player Variable(Event Player, B, Append To Array, Closest Player To(Event Player, Team 1));
		Loop If Condition Is True;
		disabled Event Player.S = Empty Array;
		disabled Loop If(Count Of(Event Player.C) == 0);
	}
}

rule("Reaper : Reset values")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Reaper;
	}

	conditions
	{
		Is Using Ultimate(Event Player) == False;
	}

	actions
	{
		Event Player.A = 0;
		Event Player.B = Null;
		Event Player.C = 0;
	}
}

rule("Reaper : AI")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Reaper;
	}

	conditions
	{
		Distance Between(Event Player, Closest Player To(Event Player, Team 1)) < 4;
		Ultimate Charge Percent(Event Player) == 100;
	}

	actions
	{
		Press Button(Event Player, Button(Ultimate));
	}
}

rule("Reaper : AURA")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		Reaper;
	}

	actions
	{
		Create Effect(All Players(All Teams), Sparkles, Color(Purple), Event Player, 1, Visible To Position and Radius);
		Create Effect(All Players(All Teams), Ring, Color(Purple), Event Player, 5, Visible To Position and Radius);
	}
}

disabled rule("Debug :")
{
	event
	{
		Ongoing - Each Player;
		All;
		All;
	}

	actions
	{
		Create HUD Text(All Players(All Teams), Global.A, Null, Null, Left, 0, Color(White), Color(White), Color(White),
			Visible To and String, Default Visibility);
	}
}

disabled rule("Show Location")
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
	}

	actions
	{
		Create HUD Text(All Players(All Teams), Position Of(Event Player), Null, Null, Left, 0, Color(White), Color(White), Color(White),
			Visible To and String, Default Visibility);
	}
}

disabled rule("If hacked do damage to Team 2")
{
	event
	{
		Ongoing - Each Player;
		Team 2;
		All;
	}

	conditions
	{
		Has Status(Event Player, Hacked) == True;
	}

	actions
	{
		Set Status(Event Player, Null, Frozen, 5);
		Start Damage Over Time(Event Player, Null, 5, 60);
	}
}