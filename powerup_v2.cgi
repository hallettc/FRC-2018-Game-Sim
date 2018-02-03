#!/usr/bin/perl -w

use CGI;
my $q = CGI->new();

my $debug = 0;

# TODO
# apply force to score
# apply boost to score

# game state variables
my $REDforce = 0;	# number of RED force cubes 0-3(4 = activated)
my $REDlevitate = 0;	# number of RED levitate cubes 0-3(4 = activated
my $REDboost = 0;	# number of RED boost cubes 0-3(4 = activated)
my $BLUEportal = 11;	# number of BLUE portal cubes 0-11
my $REDrobot1 = 1;	# RED robot 1 cube (1 to start)
my $REDrobot2 = 1;	# RED robot 2 cube (1 to start)
my $REDrobot3 = 1;	# RED robot 3 cube (1 to start)
my $pyramidL = 10;	# number of RED pyramid cubes (0-10)
my $REDswitchL = 0;	# number of cubes on L switch RED plate
my $BLUEswitchL = 0;	# number of cubes on L switch BLUE plate
my $switchL = 6;	# number of cubes at L switch (0-6)
my $REDscale = 0;	# number of cubes on RED scale plate
my $BLUEscale = 0;	# number of cubes on BLUE scale plate
my $switchR = 6;	# number of cubes at R switch (0-6)
my $REDswitchR = 0;	# number of cubes on R switch RED plate
my $BLUEswitchR = 0;	# number of cubes on R switch BLUE plate
my $pyramidR = 10;	# number of BLUE pyramid cubes (0-10) 
my $BLUErobot1 = 1;	# BLUE robot 1 cube (1 to start)
my $BLUErobot2 = 1;	# BLUE robot 2 cube (1 to start)                
my $BLUErobot3 = 1;	# BLUE robot 3 cube (1 to start)                
my $REDportal = 11;	# number of RED portal cubes 0-11               
my $BLUEforce = 0;	# number of BLUE force cubes 0-3(4 = activated) 
my $BLUElevitate = 0;	# number of BLUE levitate cubes 0-3(4 = levitate
my $BLUEboost = 0;	# number of BLUE boost cubes 0-3(4 = levitate)  
my $stage = 0;		# timed stage number                            
my $REDscore = 0;	# RED score    
my $BLUEscore = 0;	# BLUE score   
my $loop = 0;		# which pair of robots are performing actions

my $R1 = 0;		# RED robot #1 cube destination
my $R2 = 0;		# RED robot #2 cube destination
my $R3 = 0;		# RED robot #3 cube destination
my $B1 = 0;		# BLUE robot #1 cube destination
my $B2 = 0;		# BLUE robot #2 cube destination
my $B3 = 0;		# BLUE robot #3 cube destination
my $RC1 = 0;		# RED robot #1 cube source
my $RC2 = 0;		# RED robot #2 cube source
my $RC3 = 0;		# RED robot #3 cube source
my $BC1 = 0;		# BLUE robot #1 cube source
my $BC2 = 0;		# BLUE robot #2 cube source
my $BC3 = 0;		# BLUE robot #3 cube source

my $redforceUp = 0;	# RED force activated
my $redliftUp = 0;	# RED levitate activated
my $redboostUp = 0;	# RED boost activated
my $blueforceUp = 0;	# BLUE force activated
my $blueliftUp = 0;	# BLUE levitate activated
my $blueboostUp = 0;	# BLUE boost activated

# cube positions
my $REDforcePos3 = "top:135px; left:15px;";
my $REDforcePos2 = "top:165px; left:15px";
my $REDforcePos1 = "top:195px; left:15px;";
my $REDlevitatePos3 = "top:135px; left:45px;";
my $REDlevitatePos2 = "top:165px; left:45px;";
my $REDlevitatePos1 = "top:195px; left:45px;";
my $REDboostPos3 = "top:135px; left:75px;";
my $REDboostPos2 = "top:165px; left:75px;";
my $REDboostPos1 = "top:195px; left:75px;";

my $BLUEportalPos11 = "top:20px; left:105px;";
my $BLUEportalPos10 = "top:20px; left:120px;";
my $BLUEportalPos9 = "top:20px; left:135px;";
my $BLUEportalPos8 = "top:20px; left:150px;";
my $BLUEportalPos7 = "top:35px; left:105px;";
my $BLUEportalPos6 = "top:360px; left:105px;";
my $BLUEportalPos5 = "top:360px; left:120px;";
my $BLUEportalPos4 = "top:360px; left:135px;";
my $BLUEportalPos3 = "top:360px; left:150px;";
my $BLUEportalPos2 = "top:345px; left:105px;";
my $BLUEportalPos1 = "top:345px; left:120px;";

my $REDrobotPos1 = "top:95px; left:140px;";
my $REDrobotPos2 = "top:215px; left:140px;";
my $REDrobotPos3 = "top:285px; left:140px;";

my $REDpyramidPos1 = "top:205px; left:260px;";
my $REDpyramidPos2 = "top:190px; left:260px;";
my $REDpyramidPos3 = "top:175px; left:260px;";
my $REDpyramidPos4 = "top:198px; left:245px;";
my $REDpyramidPos5 = "top:182px; left:245px;";
my $REDpyramidPos6 = "top:190px; left:230px;";
my $REDpyramidPos7 = "top:198px; left:255px;";
my $REDpyramidPos8 = "top:182px; left:255px;";
my $REDpyramidPos9 = "top:190px; left:240px;";
my $REDpyramidPos10 = "top:190px; left:250px;";

my $REDswitchPos6 = "top:120px; left:330px;";
my $REDswitchPos5 = "top:148px; left:330px;";
my $REDswitchPos4 = "top:175px; left:330px;";
my $REDswitchPos3 = "top:205px; left:330px;";
my $REDswitchPos2 = "top:232px; left:330px;";
my $REDswitchPos1 = "top:260px; left:330px;";

my $BLUEswitchPos6 = "top:120px; right:340px;";
my $BLUEswitchPos5 = "top:148px; right:340px;";
my $BLUEswitchPos4 = "top:175px; right:340px;";
my $BLUEswitchPos3 = "top:205px; right:340px;";
my $BLUEswitchPos2 = "top:232px; right:340px;";
my $BLUEswitchPos1 = "top:260px; right:340px;";

my $BLUEpyramidPos1 = "top:175px; right:270px;";
my $BLUEpyramidPos2 = "top:190px; right:270px;";
my $BLUEpyramidPos3 = "top:205px; right:270px;";
my $BLUEpyramidPos4 = "top:182px; right:255px;";
my $BLUEpyramidPos5 = "top:198px; right:255px;";
my $BLUEpyramidPos6 = "top:190px; right:240px;";
my $BLUEpyramidPos7 = "top:182px; right:265px;";
my $BLUEpyramidPos8 = "top:198px; right:265px;";
my $BLUEpyramidPos9 = "top:190px; right:250px;";
my $BLUEpyramidPos10 = "top:190px; right:260px;";

my $BLUErobotPos1 = "top:95px; right:150px;";
my $BLUErobotPos2 = "top:165px; right:150px;";
my $BLUErobotPos3 = "top:285px; right:150px;";

my $REDportalPos11 = "top:20px; right:115px;";
my $REDportalPos10 = "top:20px; right:130px;";
my $REDportalPos9 = "top:20px; right:145px;";
my $REDportalPos8 = "top:20px; right:160px;";
my $REDportalPos7 = "top:35px; right:115px;";
my $REDportalPos6 = "top:360px; right:115px;";
my $REDportalPos5 = "top:360px; right:130px;";
my $REDportalPos4 = "top:360px; right:145px;";
my $REDportalPos3 = "top:360px; right:160px;";
my $REDportalPos2 = "top:345px; right:115px;";
my $REDportalPos1 = "top:345px; right:130px;";

my $BLUEforcePos3 = "top:135px; right:80px;";
my $BLUEforcePos2 = "top:165px; right:80px;";
my $BLUEforcePos1 = "top:195px; right:80px;";

my $BLUElevitatePos3 = "top:135px; right:50px;";
my $BLUElevitatePos2 = "top:165px; right:50px;";
my $BLUElevitatePos1 = "top:195px; right:50px;";

my $BLUEboostPos3 = "top:135px; right:20px;";
my $BLUEboostPos2 = "top:165px; right:20px;";
my $BLUEboostPos1 = "top:195px; right:20px;";

#               vault points|switch points|scale points
my $stage1reddata = "<TD align=center>0</TD><TD align=center>0</TD><TD align=center>0</TD>";
my $stage1bludata = "<TD align=center>0</TD><TD align=center>0</TD><TD align=center>0</TD>";


#
# read in previous game state and latest robot actions
#
if ($q->param) {
	$REDforce = $q->param('REDforce') if (defined $q->param('REDforce'));
	$REDlevitate = $q->param('REDlevitate') if (defined $q->param('REDlevitate'));
	$REDboost = $q->param('REDboost') if (defined $q->param('REDboost'));
	$BLUEportal = $q->param('BLUEportal') if (defined $q->param('BLUEportal'));
	$BLUEportal = $q->param('BLUEportal') if (defined $q->param('BLUEportal'));
	$REDrobot1 = $q->param('REDrobot1') if (defined $q->param('REDrobot1'));
	$REDrobot2 = $q->param('REDrobot2') if (defined $q->param('REDrobot2'));
	$REDrobot3 = $q->param('REDrobot3') if (defined $q->param('REDrobot3'));
	$pyramidL = $q->param('pyramidL') if (defined $q->param('pyramidL'));
	$REDswitchL = $q->param('REDswitchL') if (defined $q->param('REDswitchL'));
	$BLUEswitchL = $q->param('BLUEswitchL') if (defined $q->param('BLUEswitchL'));
	$switchL = $q->param('switchL') if (defined $q->param('switchL'));
	$REDscale = $q->param('REDscale') if (defined $q->param('REDscale'));
	$BLUEscale = $q->param('BLUEscale') if (defined $q->param('BLUEscale'));
	$switchR = $q->param('switchR') if (defined $q->param('switchR'));
	$REDswitchR = $q->param('REDswitchR') if (defined $q->param('REDswitchR'));
	$BLUEswitchR = $q->param('BLUEswitchR') if (defined $q->param('BLUEswitchR'));
	$pyramidR = $q->param('pyramidR') if (defined $q->param('pyramidR'));
	$BLUErobot1 = $q->param('BLUErobot1') if (defined $q->param('BLUErobot1'));
	$BLUErobot2 = $q->param('BLUErobot2') if (defined $q->param('BLUErobot2'));
	$BLUErobot3 = $q->param('BLUErobot3') if (defined $q->param('BLUErobot3'));
	$REDportal = $q->param('REDportal') if (defined $q->param('REDportal'));
	$REDportal = $q->param('REDportal') if (defined $q->param('REDportal'));
	$BLUEforce = $q->param('BLUEforce') if (defined $q->param('BLUEforce'));
	$BLUElevitate = $q->param('BLUElevitate') if (defined $q->param('BLUElevitate'));
	$BLUEboost = $q->param('BLUEboost') if (defined $q->param('BLUEboost'));
	$stage = $q->param('stage') if (defined $q->param('stage'));
	$REDscore = $q->param('REDscore') if (defined $q->param('REDscore'));
	$BLUEscore = $q->param('BLUEscore') if (defined $q->param('BLUEscore'));
	$R1 = $q->param('R1') if (defined $q->param('R1'));
	$R2 = $q->param('R2') if (defined $q->param('R2'));
	$R3 = $q->param('R3') if (defined $q->param('R3'));
	$B1 = $q->param('B1') if (defined $q->param('B1'));
	$B2 = $q->param('B2') if (defined $q->param('B2'));
	$B3 = $q->param('B3') if (defined $q->param('B3'));
	$RC1 = $q->param('RC1') if (defined $q->param('RC1'));
	$RC2 = $q->param('RC2') if (defined $q->param('RC2'));
	$RC3 = $q->param('RC3') if (defined $q->param('RC3'));
	$BC1 = $q->param('BC1') if (defined $q->param('BC1'));
	$BC2 = $q->param('BC2') if (defined $q->param('BC2'));
	$BC3 = $q->param('BC3') if (defined $q->param('BC3'));
	$loop = $q->param('loop') if (defined $q->param('loop'));
	$redforceUp = $q->param('redforceUp') if (defined $q->param('redforceUp'));
	$redliftUp = $q->param('redliftUp') if (defined $q->param('redliftUp'));
	$redboostUp = $q->param('redboostUp') if (defined $q->param('redboostUp'));
	$blueforceUp = $q->param('blueforceUp') if (defined $q->param('blueforceUp'));
	$blueliftUp = $q->param('blueliftUp') if (defined $q->param('blueliftUp'));
	$blueboostUp = $q->param('blueboostUp') if (defined $q->param('blueboostUp'));
	$stage1reddata = $q->param('stage1reddata') if (defined $q->param('stage1reddata'));
	$stage1bludata = $q->param('stage1bludata') if (defined $q->param('stage1bludata'));
}

#
# Helper functions
#
my $redOwnSw = 0;
my $bluOwnSw = 0;
my $redOwnSc = 0;
my $bluOwnSc = 0;

# determine ownership of switch and scale and score it
sub scoreOwnership($) {
	my ($state) = (@_);
	# if state==0, this is pre-scoring
	# if state==1, this is post-scoring

	if ($REDswitchL > $BLUEswitchL) {
		# RED owns its own switch
		$redOwnSw++;
		$REDscore += 6;
		$REDscore += 4 if ($stage == 1); # autonomous
		if ("$redboostUp" == "1") {
			# boost activated and switch owned; double the score for
			# this portion of ownership
			$REDscore += 5;
		}
	} elsif ("$redforceUp" == "1" && ($REDforce == 1 || $REDforce == 3)) {
		# force activated and switch not own; own it for this portion of
		# ownership
		$REDscore += 5;
	}

	if ($REDscale > $BLUEscale) {
		# RED owns the scale
		$redOwnSc++;
		$REDscore += 6;
		$REDscore += 4 if ($stage == 1);
		# check PowerUps
		if ("$blueforceUp" == "1" && ($BLUEforce == 2 || $BLUEforce == 3)) {
			# 20-point swing if BLUE force is activated
			$redOwnSc--;
			$REDscore  -= 5;
		}
		if ("$redboostUp" == "1") {
			# boost activated and scale owned; double the score for
			# this portion of ownership
			$REDscore += 5;
		}
	} elsif ("$redforceUp" == "1" && ($REDforce == 2 || $REDforce == 3)) {
		# RED force is activated on scale, provide credit
		$redOwnSc++;
		$REDscore += 5;
	}

	if ($REDscale < $BLUEscale) {
		# BLUE owns the scale
		$bluOwnSc++;
		$BLUEscore += 6;
		$BLUEscore += 4 if ($stage == 1);
		# check PowerUps
		if ("$redforceUp" == "1" && ($REDforce == 2 || $REDforce == 3)) {
			# RED force is activated, remove 5 from BLUE score
			$bluOwnSc--;
			$BLUEscore -= 5;
		}
		if ("$blueboostUp" == "1") {
			# boost activated and scale owned; double the score for
			# this portion of ownership
			$BLUEscore += 5;
		}
	} elsif ("$blueforceUp" == "1" && ($BLUEforce == 2 || $BLUEforce == 3)) {
		# BLUE force is activated on scale, provide credit
		$bluOwnSc++;
		$BLUEscore += 5;
	}

	if ($REDswitchR < $BLUEswitchR) {
		# BLUE owns its own switch
		$bluOwnSw++;
		$BLUEscore += 6;
		$BLUEscore += 4 if ($stage == 1); # autonomous
		if ("$blueboostUp" == "1") {
			# boost activated and switch owned; double the score for
			# this portion of ownership
			$BLUEscore += 5;
		}
	} elsif ("$blueforceUp" == "1" && ($BLUEforce == 1 || $BLUEforce == 3)) {
		# force activated and switch not own; own it for this portion of
		# ownership
		$bluOwnSw++;
		$BLUEscore += 5;
	}
}

sub scoreRedAction($) {
	my ($action) = (@_);

	# update counts on the switch and scale
	$REDswitchL++ if ($action == 1);
	$REDscale++   if ($action == 2);
	$REDswitchR++ if ($action == 3);

	# update counts on the vault
	if ($action == 4) {
		if ($REDforce < 3) {
			$REDforce++;
			$REDscore += 5;
		} else {
			$REDportal++;
		}
	}
	if ($action == 5) {
		if ($REDlevitate < 3) {
			$REDlevitate++;
			$REDscore += 5;
		} else {
			$REDportal++;
		}
	}
	if ($action == 6) {
		if ($REDboost < 3) {
			$REDboost++;
			$REDscore += 5;
		} else {
			$REDportal++;
		}
	}
}

sub scoreBlueAction($) {
	my ($action) = (@_);

	# update counts on the switch and scale
	$BLUEswitchR++ if ($action == 1);
	$BLUEscale++   if ($action == 2);
	$BLUEswitchL++ if ($action == 3);

	# update counts on the vault
	if ($action == 4) {
		if ($BLUEforce < 3) {
			$BLUEforce++;
			$BLUEscore += 5;
		} else {
			$BLUEportal++;
		}
	}
	if ($action == 5) {
		if ($BLUElevitate < 3) {
			$BLUElevitate++;
			$BLUEscore += 5;
		} else {
			$BLUEportal++;
		}
	}
	if ($action == 6) {
		if ($BLUEboost < 3) {
			$BLUEboost++;
			$BLUEscore += 5;
		} else {
			$BLUEportal++;
		}
	}
}

# remove cubes from locations
sub removeCubes($$) {
	my ($robot, $color) = (@_);
	$pyramidL-- if ("$color" eq "red" && $robot == 1);
	$switchL-- if ("$color" eq "red" && $robot == 2);
	$pyramidR-- if ("$color" eq "blue" && $robot == 1);
	$switchR-- if ("$color" eq "blue" && $robot == 2);
	$REDportal-- if ("$color" eq "red" && $robot == 3 && $REDportal > 0);
	$BLUEportal-- if ("$color" eq "blue" && $robot == 3 && $BLUEportal > 0);
}

sub printCube($) {
	my ($cubepos) = (@_);
	print "<div style=\"position:absolute; $cubepos\"><IMG SRC=cube.png></div>\n"
}

# increment loop
$loop += 1;

if ($loop > 3) {
	# end of the loop
	$loop = 1;
	
	# increment the time stage
	$stage += 1;

	# queue up multiple PowerUps!
	# 'force' happens before 'boost', unless 'boost' has been queued up

	# if same color boost and force are active, force goes first 
	if ($redboostUp == 1 && $redforceUp == 1) {
		# force goes first
		$redboostUp = 0;
	}
	if ($blueboostUp == 1 && $blueforceUp == 1) {
		# force goes first
		$blueboostUp = 0;
	}

	if ($redforceUp == 1 && $blueforceUp == 1) {
		# red force goes first
		$blueforceUp = 0;	
	}
	if ($redforceUp == 1 && $blueboostUp == 1) {
		# blue boost goes first
		$redforceUp = 0;
	}
	if ($reboostUp == 1 && $blueforceUp == 1) {
		# blue force up goes first
		$redboostUp = 0;
	}
	if ($redboostUp == 1 && $blueboostUp == 1) {
		# red boost goes first
		$blueboostUp == 0;
	}


	# process latest robot actions after all 3 have submitted actions
	# ownership is calculated twice (before and after action) with
	# half-score each to split scoring on a change of ownership
	scoreOwnership(0);
	scoreRedAction($R1);
	scoreRedAction($R2);
	scoreRedAction($R3);
	scoreBlueAction($B1);
	scoreBlueAction($B2);
	scoreBlueAction($B3);
	scoreOwnership(1);
	# clear/adjust any PowerUps!
	if ($redforceUp == 1) {
		$redforceUp = 0;
		$REDforce++;
	}
	if ($redboostUp == 1) {
		$redboostUp = 0;
		$REDboost++;
	}
	if ($blueforceUp == 1) {
		$blueforceUp = 0;
		$BLUEforce++;
	}
	if ($blueboostUp == 1) {
		$blueboostUp = 0;
		$BLUEboost++;
	}
}


# score levitate as soon as its activated
if ($redliftUp == 1) {
	$REDlevitate++;
	$REDscore += 30;
}
if ($blueliftUp == 1) {
	$BLUElevitate++;
	$BLUEscore += 30;
}
# score climbs at endgame
if ($stage > 9) {
	$REDscore  += 60;
	$BLUEscore += 60;
	$REDscore  += 30 if ($REDlevitate < 4);
	$BLUEscore += 30 if ($BLUElevitate < 4);
}

# store the data
if ($stage == 1) {
	my $vault = ($REDforce + $REDlevitate + $REDboost) * 5;
	$stage1reddata = "<TD align=center>$vault</TD><TD align=center>$redOwnSw</TD><TD align=center>$redOwnSc</TD>";
	$vault = ($BLUEforce + $BLUElevitate + $BLUEboost) * 5;
	$stage1bludata = "<TD align=center>$vault</TD><TD align=center>$bluOwnSw</TD><TD align=center>$bluOwnSc</TD>";
}

# remove cubes from latest robot actions
removeCubes($RC1, "red");
removeCubes($RC2, "red");
removeCubes($RC3, "red");
removeCubes($BC1, "blue");
removeCubes($BC2, "blue");
removeCubes($BC3, "blue");


#
# Print the web page
#
print "Content-type: text/html\n\n";
print "<html><head>\n";
print "<title>FIRST Power Up!</title>\n";
print "<link rel='SHORTCUT ICON' href='favicon.ico'>\n";
print "<link rel='apple-touch-icon' href='favicon.png'>\n";
print "<meta name='description' content='FIRST Robotics Team 1073, Power Up Strategy Game'>\n";
print "<meta name='keywords' content='FIRST, Robotics, 1073, The Force Team, Power Up, Strategy Game'>\n";
print "<meta name='author' content='FIRST Team 1073'>\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n";
print "</head>\n";
print "<body><center>\n";
print "<H1><I>FIRST</I> PowerUp! Strategy Game</H1>\n";

#
# submit the updated game status
#
print "<FORM METHOD=\"post\" ACTION=\"newpower.cgi\">\n";
print "<input type=\"hidden\" name=\"REDforce\" value=\"$REDforce\">\n";
print "<input type=\"hidden\" name=\"REDlevitate\" value=\"$REDlevitate\">\n";
print "<input type=\"hidden\" name=\"REDboost\" value=\"$REDboost\">\n";
print "<input type=\"hidden\" name=\"BLUEportal\" value=\"$BLUEportal\">\n";
print "<input type=\"hidden\" name=\"REDrobot1\" value=\"$REDrobot1\">\n";
print "<input type=\"hidden\" name=\"REDrobot2\" value=\"$REDrobot2\">\n";
print "<input type=\"hidden\" name=\"REDrobot3\" value=\"$REDrobot3\">\n";
print "<input type=\"hidden\" name=\"pyramidL\" value=\"$pyramidL\">\n";
print "<input type=\"hidden\" name=\"REDswitchL\" value=\"$REDswitchL\">\n";
print "<input type=\"hidden\" name=\"BLUEswitchL\" value=\"$BLUEswitchL\">\n";
print "<input type=\"hidden\" name=\"switchL\" value=\"$switchL\">\n";
print "<input type=\"hidden\" name=\"REDscale\" value=\"$REDscale\">\n";
print "<input type=\"hidden\" name=\"BLUEscale\" value=\"$BLUEscale\">\n";
print "<input type=\"hidden\" name=\"switchR\" value=\"$switchR\">\n";
print "<input type=\"hidden\" name=\"REDswitchR\" value=\"$REDswitchR\">\n";
print "<input type=\"hidden\" name=\"BLUEswitchR\" value=\"$BLUEswitchR\">\n";
print "<input type=\"hidden\" name=\"pyramidR\" value=\"$pyramidR\">\n";
print "<input type=\"hidden\" name=\"BLUErobot1\" value=\"$BLUErobot1\">\n";
print "<input type=\"hidden\" name=\"BLUErobot2\" value=\"$BLUErobot2\">\n";
print "<input type=\"hidden\" name=\"BLUErobot3\" value=\"$BLUErobot3\">\n";
print "<input type=\"hidden\" name=\"REDportal\" value=\"$REDportal\">\n";
print "<input type=\"hidden\" name=\"BLUEforce\" value=\"$BLUEforce\">\n";
print "<input type=\"hidden\" name=\"BLUElevitate\" value=\"$BLUElevitate\">\n";
print "<input type=\"hidden\" name=\"BLUEboost\" value=\"$BLUEboost\">\n";
print "<input type=\"hidden\" name=\"stage\" value=\"$stage\">\n";
print "<input type=\"hidden\" name=\"REDscore\" value=\"$REDscore\">\n";
print "<input type=\"hidden\" name=\"BLUEscore\" value=\"$BLUEscore\">\n";
print "<input type=\"hidden\" name=\"loop\" value=\"$loop\">\n";
# need to preserve robot movements from loop 1 and 2 for scoring after 3
print "<input type=\"hidden\" name=\"R1\" value=\"$R1\">\n" if ($loop == 2 || $loop == 3);
print "<input type=\"hidden\" name=\"B1\" value=\"$B1\">\n" if ($loop == 2 || $loop == 3);
print "<input type=\"hidden\" name=\"R2\" value=\"$R2\">\n" if ($loop == 3);
print "<input type=\"hidden\" name=\"B2\" value=\"$B2\">\n" if ($loop == 3);
# need to preserve powerUps activated in loop 1 for scoring after loop 3
if ($loop == 2 || $loop == 3) {
	print "<input type=\"hidden\" name=\"redforceUp\" value=\"$redforceUp\">\n";
	print "<input type=\"hidden\" name=\"redboostUp\" value=\"$redboostUp\">\n";
	print "<input type=\"hidden\" name=\"blueforceUp\" value=\"$blueforceUp\">\n";
	print "<input type=\"hidden\" name=\"blueboostUp\" value=\"$blueboostUp\">\n";
}
print "<input type=\"hidden\" name=\"stage1reddata\" value=\"$stage1reddata\">\n";
print "<input type=\"hidden\" name=\"stage1bludata\" value=\"$stage1bludata\">\n";

#
# print the updated field
#
print "<table cellspacing=0 cellpadding=0 border=0><tr><td colspan=2>\n";
print "<div style=\"position:relative; background:url(field.png); no-repeat left top; width: 917px; height:477px;\">\n";

# print switch/scale scoring                                                                          
print "<div style=\"position:absolute; top:132px; left:290px; color:yellow;\"><B>$REDswitchL</B></div>\n";
print "<div style=\"position:absolute; top:242px; left:290px; color:yellow;\"><B>$BLUEswitchL</B></div>\n";
print "<div style=\"position:absolute; top:115px; left:445px; color:yellow;\"><B>$BLUEscale</B></div>\n";
print "<div style=\"position:absolute; top:260px; left:445px; color:yellow;\"><B>$REDscale</B></div>\n";
print "<div style=\"position:absolute; top:132px; right:300px; color:yellow;\"><B>$REDswitchR</B></div>\n";
print "<div style=\"position:absolute; top:242px; right:300px; color:yellow;\"><B>$BLUEswitchR</B></div>\n";

# print all of the cubes
printCube($REDforcePos3) if ($REDforce > 2);
printCube($REDforcePos2) if ($REDforce > 1);
printCube($REDforcePos1) if ($REDforce > 0);
printCube($REDlevitatePos3) if ($REDlevitate > 2);
printCube($REDlevitatePos2) if ($REDlevitate > 1);
printCube($REDlevitatePos1) if ($REDlevitate > 0);
printCube($REDboostPos3) if ($REDboost > 2);
printCube($REDboostPos2) if ($REDboost > 1);
printCube($REDboostPos1) if ($REDboost > 0);

printCube($BLUEportalPos11) if ($BLUEportal > 10);
printCube($BLUEportalPos10) if ($BLUEportal > 9);
printCube($BLUEportalPos9) if ($BLUEportal > 8);
printCube($BLUEportalPos8) if ($BLUEportal > 7);
printCube($BLUEportalPos7) if ($BLUEportal > 6);
printCube($BLUEportalPos6) if ($BLUEportal > 5);
printCube($BLUEportalPos5) if ($BLUEportal > 4);
printCube($BLUEportalPos4) if ($BLUEportal > 3);
printCube($BLUEportalPos3) if ($BLUEportal > 2);
printCube($BLUEportalPos2) if ($BLUEportal > 1);
printCube($BLUEportalPos1) if ($BLUEportal > 0);

if ($stage == 0) {
	printCube($REDrobotPos1) if ($loop < 2);
	printCube($REDrobotPos2) if ($loop < 3);
	printCube($REDrobotPos3);
}

printCube($REDpyramidPos1) if ($pyramidL > 0);
printCube($REDpyramidPos2) if ($pyramidL > 1);
printCube($REDpyramidPos3) if ($pyramidL > 2);
printCube($REDpyramidPos4) if ($pyramidL > 3);
printCube($REDpyramidPos5) if ($pyramidL > 4);
printCube($REDpyramidPos6) if ($pyramidL > 5);
printCube($REDpyramidPos7) if ($pyramidL > 6);
printCube($REDpyramidPos8) if ($pyramidL > 7);
printCube($REDpyramidPos9) if ($pyramidL > 8);
printCube($REDpyramidPos10) if ($pyramidL > 9);

printCube($REDswitchPos6) if ($switchL > 5);
printCube($REDswitchPos5) if ($switchL > 4);
printCube($REDswitchPos4) if ($switchL > 3);
printCube($REDswitchPos3) if ($switchL > 2);
printCube($REDswitchPos2) if ($switchL > 1);
printCube($REDswitchPos1) if ($switchL > 0);

printCube($BLUEswitchPos6) if ($switchR > 5);
printCube($BLUEswitchPos5) if ($switchR > 4);
printCube($BLUEswitchPos4) if ($switchR > 3);
printCube($BLUEswitchPos3) if ($switchR > 2);
printCube($BLUEswitchPos2) if ($switchR > 1);
printCube($BLUEswitchPos1) if ($switchR > 0);

printCube($BLUEpyramidPos1) if ($pyramidR > 0);
printCube($BLUEpyramidPos2) if ($pyramidR > 1);
printCube($BLUEpyramidPos3) if ($pyramidR > 2);
printCube($BLUEpyramidPos4) if ($pyramidR > 3);
printCube($BLUEpyramidPos5) if ($pyramidR > 4);
printCube($BLUEpyramidPos6) if ($pyramidR > 5);
printCube($BLUEpyramidPos7) if ($pyramidR > 6);
printCube($BLUEpyramidPos8) if ($pyramidR > 7);
printCube($BLUEpyramidPos9) if ($pyramidR > 8);
printCube($BLUEpyramidPos10) if ($pyramidR > 9);

if ($stage == 0) {
	printCube($BLUErobotPos1) if ($loop < 2);
	printCube($BLUErobotPos2) if ($loop < 3);
	printCube($BLUErobotPos3);
}

printCube($REDportalPos11) if ($REDportal > 10);
printCube($REDportalPos10) if ($REDportal > 9);
printCube($REDportalPos9) if ($REDportal > 8);
printCube($REDportalPos8) if ($REDportal > 7);
printCube($REDportalPos7) if ($REDportal > 6);
printCube($REDportalPos6) if ($REDportal > 5);
printCube($REDportalPos5) if ($REDportal > 4);
printCube($REDportalPos4) if ($REDportal > 3);
printCube($REDportalPos3) if ($REDportal > 2);
printCube($REDportalPos2) if ($REDportal > 1);
printCube($REDportalPos1) if ($REDportal > 0);

printCube($BLUEforcePos3) if ($BLUEforce > 2);
printCube($BLUEforcePos2) if ($BLUEforce > 1);
printCube($BLUEforcePos1) if ($BLUEforce > 0);

printCube($BLUElevitatePos3) if ($BLUElevitate > 2);
printCube($BLUElevitatePos2) if ($BLUElevitate > 1);
printCube($BLUElevitatePos1) if ($BLUElevitate > 0);

printCube($BLUEboostPos3) if ($BLUEboost > 2);
printCube($BLUEboostPos2) if ($BLUEboost > 1);
printCube($BLUEboostPos1) if ($BLUEboost > 0);

#
# print the current score and the time
#
print "</div></td></tr><tr>\n";
print "<td colspan=2>";
print "<table width=\"100%\" border=0><tr>";
print "<th><H3><div style=\"color:red\">Red Alliance: $REDscore</div></H3>\n";
my $time = "2:30";
$time = "2:15" if ($stage == 1);
$time = "2:03" if ($stage == 2);
$time = "1:51" if ($stage == 3);
$time = "1:39" if ($stage == 4);
$time = "1:27" if ($stage == 5);
$time = "1:15" if ($stage == 6);
$time = "1:03" if ($stage == 7);
$time = " :51" if ($stage == 8);
$time = " :39" if ($stage == 9);
$time = " :27" if ($stage == 10);
$time = " :00" if ($stage > 10);
print "</th><th>Time: $time</th><th>\n";
print "<H3><div style=\"color:blue\">Blue Alliance: $BLUEscore</div></H3>\n";
print "</tr></table></td></tr>\n";

#
# helper functions for printing the robot actions
#
sub printSelection($) {
	my ($pick) = (@_);
	
	print "nowhere" if ($pick < 1);
	print "pyramid" if ($pick == 1);
	print "switch edge" if ($pick == 2);
	print "portal" if ($pick == 3);
}

sub printDestination($$) {
	my ($color, $pick) = (@_);
	
	print "nowhere" if ($pick < 1);
	print "own switch $color plate" if ($pick == 1);
	print "scale $color plate" if ($pick == 2);
	print "opposing switch $color plate" if ($pick == 3);
	print "exchange" if ($pick > 3);
}

sub DisplaySelection($$$$) {
	my ($color, $num, $robot, $cube) = (@_);
	# "red", "1" "$R1" "$RC1"

	my $alliance = "Red";
	if ("$color" eq "blue") {
		$alliance = "Blue";
	}
	if ($stage == 0) {
		print "<p>$alliance #$num moved its cube to ";
	} else {
		print "<p>$alliance #$num from ";
		printSelection($cube);
		print " to ";
	}
	printDestination("$color", $robot);
}

sub DisplayOptions($$$$) {
	my ($color, $num, $robot, $cube) = (@_);
	# "red", "1" "R1" "RC1"
	
	my $alliance = "Red";
	my $pyramid  = $pyramidL;
	my $switch   = $switchL;
	my $portal   = $REDportal;
	my $force    = $REDforce;
	my $levitate = $REDlevitate;
	my $boost    = $REDboost;
	# check if previous robot selections loaded exchange
	my $preForce = 0;
	$preForce++ if ($num > 1 && $R1 == 4);
	$preForce++ if ($num > 2 && $R2 == 4);
	my $preLift  = 0;
	$preLift++  if ($num > 1 && $R1 == 5);
	$preLift++  if ($num > 2 && $R2 == 5);
	my $preBoost = 0;
	$preBoost++ if ($num > 1 && $R1 == 6);
	$preBoost++ if ($num > 2 && $R2 == 6);
	if ("$color" eq "blue") {
		$alliance = "Blue";
		$pyramid  = $pyramidR;
		$switch   = $switchR;
		$portal   = $BLUEportal;
		$force    = $BLUEforce;
		$levitate = $BLUElevitate;
		$boost    = $BLUEboost;
		$preForce = 0;
		$preForce++ if ($num > 1 && $B1 == 4);
		$preForce++ if ($num > 2 && $B2 == 4);
		$preLift  = 0;
		$preLift++  if ($num > 1 && $B1 == 5);
		$preLift++  if ($num > 2 && $B2 == 5);
		$preBoost = 0;
		$preBoost++ if ($num > 1 && $B1 == 6);
		$preBoost++ if ($num > 2 && $B2 == 6);
	}
	print "<table cellpadding=0 cellspacing=0 border=1><tr><td>";
	print "<table cellpadding=0 cellspacing=0 border=0><tr><td>";
	# print autonomous actions
	if ($stage == 0) {
		print "<p><b>$alliance Robot #$num<br>places its cube on</b></p>";
	} else {
		my $fchecked = "CHECKED=yes";
		my $lchecked = "";
		my $bchecked = "";
		$lchecked = "CHECKED=yes" if ($pyramid < 1);
		$bchecked = "CHECKED=yes" if ($pyramid < 1 && $switch < 1);
		print "<p><b>$alliance Robot #$num from</b><br>";
		print "<table cellpadding=0 cellspacing=0 border=0><tr><td>\n";
		print "<INPUT TYPE=\"radio\" NAME=\"$cube\" VALUE=\"1\" $fchecked>pyramid<br>\n" if ($pyramid > 0);
		print "<INPUT TYPE=\"radio\" NAME=\"$cube\" VALUE=\"2\" $lchecked>switch edge<br>\n" if ($switch > 0);
		print "<INPUT TYPE=\"radio\" NAME=\"$cube\" VALUE=\"3\" $bchecked>portal\n" if ($portal > 0);
		print "</td><td align=center valign=center>&nbsp;&nbsp;<b>to</b></td></tr></table>\n";
	}
	print "</td><td>";
	print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"1\" CHECKED=yes>$color plate on own SWITCH<br>\n";
	print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"2\" >$color plate on SCALE<br>\n";
	print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"3\" >$color plate on opposing SWITCH<br>\n" if ($stage > 0);
	if ($force + $preForce < 3) {
		print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"4\">exchange/vault for Force<br>\n";
	} else {
		print "&nbsp;<br>\n";
	}
	if ($levitate + $preLift < 3) {
		print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"5\">exchange/vault for Levitate<br>\n";
	} else {
		print "&nbsp;<br>\n";
	}
	if ($boost + $preBoost < 3) {
		print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"6\">exchange/vault for Boost<br>\n";
	} else {
		print "&nbsp;<br>\n";
	}	
	print "</td></tr><tr><td colspan=2 align=center>\n";
	if ($loop == 1) {
		my $space = "&nbsp;&nbsp;&nbsp;&nbsp;";
		print "<INPUT TYPE=\"checkbox\" NAME=\"${color}forceUp\" VALUE=\"1\">Force Up!$space\n" if ($force == 3);
		print "<INPUT TYPE=\"checkbox\" NAME=\"${color}liftUp\" VALUE=\"1\">Levitate Up!$space\n" if ($levitate == 3);
		print "<INPUT TYPE=\"checkbox\" NAME=\"${color}boostUp\" VALUE=\"1\">Boost Up!$space\n" if ($boost == 3);
		print "&nbsp;\n" if ($force != 3 && $levitate != 3 && $boost != 3);
	}
	print "</td></tr></table>\n";
	print "</td></tr></table>\n";
}


#
# print the robot "selected actions" and actions to select (depending on the loop)
# if "stage == 0" then we are in autonomous and the robot is preloaded
# else the robot needs to get a cube from somewhere before placing it
#

# if $stage 10 then we are going to climb!
if ($stage > 9) {
	# end game
	print "<tr><td align=center><p>Red Robot #1 climbs the tower!</p></td>\n";
	print "<td align=center><p>Blue Robot #1 climbs the tower!</p></td></tr>\n";
	print "<tr><td align=center><p>Red Robot #2 climbs the tower!</p></td>\n";
	print "<td align=center><p>Blue Robot #2 climbs the tower!</p></td></tr>\n";
	print "<tr><td align=center>\n";
	if ($REDlevitate < 4) {
		print "<p>Red Robot #3 climbs the tower!</p>";
	} else {
		print "&nbsp;";
	}
	print "</td><td align=center>";
	if ($BLUElevitate < 4) {
		print "<p>Blue Robot #3 climbs the tower!</p>";
	} else {
		print "&nbsp;";
	}
	print "</tr>\n";
	print "</table></BODY></HTML>\n";
	exit(0);
}
print "<tr><td align=center>\n";
if ($loop == 1) {
	DisplayOptions("red", "1", "R1", "RC1");

	print "</td><td align=center>\n";

	DisplayOptions("blue", "1", "B1", "BC1");
} else {
	# if not 'loop == 1' then both #1 robots have already acted
	# print their actions as a reminder
	DisplaySelection("red", "1", $R1, $RC1);

	print "</td><td align=center>\n";

	DisplaySelection("blue", "1", $B1, $BC1);
}
print "</td></tr><tr><td align=center>\n";
if ($loop == 2) {
	DisplayOptions("red", "2", "R2", "RC2");
		
	print "</td><td align=center>\n";
	
	DisplayOptions("blue", "2", "B2", "BC2");
} else {
	# if not 'loop == 2' then print state of both #2 robots
	if ($loop == 1) {
		# no actions taken yet: just print placeholders
		print "<p>Red Robot #2</p></td><td align=center><p>Blue Robot #2</p>";
	} else {
		# actions have been taken: print them
		DisplaySelection("red", "2", $R2, $RC2);

		print "</td><td align=center>\n";

		DisplaySelection("blue", "2", $B2, $BC2);
	}
}
print "</td></tr><tr><td align=center>";
if ($loop == 3) {
	DisplayOptions("red", "3", "R3", "RC3");

	print "</td><td align=center>\n";
	
	DisplayOptions("blue", "3", "B3", "BC3");
} else {
	print "<p>Red Robot #3</p></td><td align=center><p>Blue Robot #3</p>";
}

#
# finish the webpage with submit button
#
print "</td></tr><tr><td colspan=2 align=center><p>\n";
print "<input type=\"submit\" value=\"Submit Selections\">\n";
print "</p></tr></table>\n";
print "<p>&nbsp;</p>\n";

print "<H4>Game Introduction</H4>\n";
print "</center>\n";
print "<p>This game is designed to focus on alliance strategy, specifically, how to prioritize the\n";
print "actions of each robot. This game allows you to play out a strategy for each alliance and\n";
print "see how that strategy will impact the score. For example, you can focus the Red Alliance on\n";
print "switch and scale, and the Blue Alliance on switch and vault, just to see who would win. Or\n";
print "you can focus the Red Alliance on both switches while the Blue Alliance works on the scale\n";
print "and defending its switch.</p>\n";
print "Since this game is focused on strategy only, there are no technical advantages or technical\n";
print "limitations to either side (in real life, those are being handled by the teams building the\n";
print "robot!). Each robot is capable of gathering a cube from anywhere, and placing it anywhere,\n";
print "in the allotted time for that round. At the end of this game, all 60 cubes will be placed\n";
print "somewhere and all robots will climb the tower to \"face the boss\".</p>";
print "<center>\n";
print "<H4>Game Operation</H4>\n";
print "</center>\n";
print "<p>This game is played in increments of time. Within each \"chunk\" of time all 6 robots\n";
print "gather and place a cube. For example, the autonomous period is one 15-second \"chunk\" of\n";
print "time where these robots will only be able to place their pre-loaded cube in one of the\n";
print "designated areas. During \"teleop\" there are 9 rounds that each consume 12-seconds\n";
print "where robots gather and place cubes. The \"end game\" is the remaining 27 seconds where all\n";
print "6 robots climb the tower. This is where the final score is printed.</p>\n";
print "<p>The score is updated between each \"chunk\" of time. The score does not get updated until\n";
print "all 6 robots have submitted their actions. The only exception is the \"Levitation PowerUp!,\n";
print "which adds 30 points to the score as soon as it is activated.</p>\n";
print "<p>At this time, the scoring does NOT exactly match the actual game. Currently the scoring\n";
print "is as follows: 5 points for each cube in the vault; 10 points for taking ownship of a switch\n";
print "or scale during autonomous; 6 points per round for taking/losing ownership of a switch or\n";
print "scale; 12 points for full ownership of a switch or scale during a round; 30 points for a\n";
print "climb (either at \"end game\" or via levitation \"powerUp!\"). Appropriate points for\n";
print "activated \"Boost\" and \"Force\" PowerUps.</p>\n";
print "<p>The \"PowerUps!\" can only be activated at the beginning of each round. One limitation of\n";
print "this game: if multiple PowerUps are activated and one or more are to be queued, this game\n";
print "picks one and clears the others, which means you will need to re-activate those powerUps.</p>\n";
print "<p><b>Disclaimer</b>: I am not perfect, so neither is my coding. Apologies in advance. :-)</p>";
print "<center>\n";
print "<H4>Play For Real!</H4>\n";


# add debugging
if ($debug) {
	print "<H5>Debug info</H5>\n";
	print "<p>loop = $loop</p>\n";
	print "<p>stage = $stage</p>\n";
	print "<p>R1 = $R1, B1 = $B1</p>\n";
	print "<p>R2 = $R2, B2 = $B2</p>\n";
	print "<p>R3 = $R3, B3 = $B3</p>\n";
	print "<p>REDforce = $REDforce, BLUEforce = $BLUEforce</p>\n";
	print "<p>REDlevitate = $REDlevitate, BLUElevitate = $BLUElevitate</p>\n";
	print "<p>REDboost = $REDboost, BLUEboost = $BLUEboost</p>\n";
	print "<p>redforceUp = $redforceUp, blueforceUp = $blueforceUp</p>\n";
	print "<p>redliftUp = $redliftUp, blueliftUp = $blueliftUp</p>\n";
	print "<p>redboostUp = $redboostUp, blueboostUp = $blueboostUp</p>\n";
	
}
print "</BODY></HTML>\n";


