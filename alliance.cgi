#!/usr/bin/perl -w

my $debug = 1;

use CGI;
my $q = CGI->new();

# game state variables
my $REDforce = 0;		# number of RED force cubes 0-3(4 = activated)
my $REDlevitate = 0;	# number of RED levitate cubes 0-3(4 = activated
my $REDboost = 0;		# number of RED boost cubes 0-3(4 = activated)
my $BLUEportal = 11;	# number of BLUE portal cubes 0-11
my $REDrobot1 = 1;		# RED robot 1 cube (1 to start)
my $REDrobot2 = 1;		# RED robot 2 cube (1 to start)
my $REDrobot3 = 1;		# RED robot 3 cube (1 to start)
my $pyramidL = 10;		# number of RED pyramid cubes (0-10)
my $REDswitchL = 0;		# number of cubes on L switch RED plate
my $BLUEswitchL = 0;	# number of cubes on L switch BLUE plate
my $switchL = 6;		# number of cubes at L switch (0-6)
my $REDscale = 0;		# number of cubes on RED scale plate
my $BLUEscale = 0;		# number of cubes on BLUE scale plate
my $switchR = 6;		# number of cubes at R switch (0-6)
my $REDswitchR = 0;		# number of cubes on R switch RED plate
my $BLUEswitchR = 0;	# number of cubes on R switch BLUE plate
my $pyramidR = 10;		# number of BLUE pyramid cubes (0-10) 
my $BLUErobot1 = 1;		# BLUE robot 1 cube (1 to start)
my $BLUErobot2 = 1;		# BLUE robot 2 cube (1 to start)                
my $BLUErobot3 = 1;		# BLUE robot 3 cube (1 to start)                
my $REDportal = 11;		# number of RED portal cubes 0-11               
my $BLUEforce = 0;		# number of BLUE force cubes 0-3(4 = activated) 
my $BLUElevitate = 0;	# number of BLUE levitate cubes 0-3(4 = levitate
my $BLUEboost = 0;		# number of BLUE boost cubes 0-3(4 = levitate)  
my $round = 0;			# round number                            
my $REDscore = 0;		# RED score    
my $BLUEscore = 0;		# BLUE score   

my $R1 = 0;				# RED  robot #1 cube destination
my $R2 = 0;				# RED  robot #2 cube destination
my $R3 = 0;				# RED  robot #3 cube destination
my $B1 = 0;				# BLUE robot #1 cube destination
my $B2 = 0;				# BLUE robot #2 cube destination
my $B3 = 0;				# BLUE robot #3 cube destination
my $RC1 = 0;			# RED  robot #1 cube source
my $RC2 = 0;			# RED  robot #2 cube source
my $RC3 = 0;			# RED  robot #3 cube source
my $BC1 = 0;			# BLUE robot #1 cube source
my $BC2 = 0;			# BLUE robot #2 cube source
my $BC3 = 0;			# BLUE robot #3 cube source

my $turn = 0;			# who's turn is it? 0/1=red, 2=blue

my $redforceUp = 0;		# RED force activated
my $redliftUp = 0;		# RED levitate activated
my $redboostUp = 0;		# RED boost activated
my $blueforceUp = 0;	# BLUE force activated
my $blueliftUp = 0;		# BLUE levitate activated
my $blueboostUp = 0;	# BLUE boost activated
my $redfUp = 0;			# RED force activated
my $redlUp = 0;			# RED levitate activated
my $redbUp = 0;			# RED boost activated
my $bluefUp = 0;		# BLUE force activated
my $bluelUp = 0;		# BLUE levitate activated
my $bluebUp = 0;		# BLUE boost activated


# static cube positions
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

# scoring table
# red_switch red_scale blue_scale blue_switch
my $begin = "<tr><td colspan=3>&nbsp;</td><td align=center>0</td><td align=center>0</td><td align=center>0</td><td align=center>0</td><td colspan=3>&nbsp;</td></tr>\n";
my $round0x = $begin;
my $round1x = $begin;
my $round2x = $begin;
my $round3x = $begin;
my $round4x = $begin;
my $round5x = $begin;
my $round6x = $begin;
my $round7x = $begin;
my $round8x = $begin;
my $round9x = $begin;


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
    $round = $q->param('round') if (defined $q->param('round'));
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
    $turn = $q->param('turn') if (defined $q->param('turn'));
	$redforceUp = $q->param('redforceUp') if (defined $q->param('redforceUp'));
	$redliftUp  = $q->param('redliftUp')  if (defined $q->param('redliftUp'));
	$redboostUp = $q->param('redboostUp') if (defined $q->param('redboostUp'));
	$blueforceUp = $q->param('blueforceUp') if (defined $q->param('blueforceUp'));
	$blueliftUp  = $q->param('blueliftUp')  if (defined $q->param('blueliftUp'));
	$blueboostUp = $q->param('blueboostUp') if (defined $q->param('blueboostUp'));
	$redfUp  = $q->param('redfUp') if (defined $q->param('redfUp'));
	$redlUp  = $q->param('redlUp') if (defined $q->param('redlUp'));
	$redbUp  = $q->param('redbUp') if (defined $q->param('redbUp'));
	$bluefUp = $q->param('bluefUp') if (defined $q->param('bluefUp'));
	$bluelUp = $q->param('bluelUp') if (defined $q->param('bluelUp'));
	$bluebUp = $q->param('bluebUp') if (defined $q->param('bluebUp'));
    $round0x = $q->param('round0x') if (defined $q->param('round0x'));
    $round1x = $q->param('round1x') if (defined $q->param('round1x'));
    $round2x = $q->param('round2x') if (defined $q->param('round2x'));
    $round3x = $q->param('round3x') if (defined $q->param('round3x'));
    $round4x = $q->param('round4x') if (defined $q->param('round4x'));
    $round5x = $q->param('round5x') if (defined $q->param('round5x'));
    $round6x = $q->param('round6x') if (defined $q->param('round6x'));
    $round7x = $q->param('round7x') if (defined $q->param('round7x'));
    $round8x = $q->param('round8x') if (defined $q->param('round8x'));
    $round9x = $q->param('round9x') if (defined $q->param('round9x'));
}

# update powerUps
$redforceUp++ if ($redfUp == 1);
$redliftUp++  if ($redlUp == 1);
$redboostUp++ if ($redbUp == 1);
$blueforceUp++ if ($bluefUp == 1);
$blueliftUp++  if ($bluelUp == 1);
$blueboostUp++ if ($bluebUp == 1);


#
# helper functions for scoring
#
my $redOwnSw = 0;
my $bluOwnSw = 0;
my $redOwnSc = 0;
my $bluOwnSc = 0;

# determine 1/2-cycle ownership of switch and scale and score it
sub scoreOwnership($) {
	my ($state) = (@_);
	# if state==0, this is pre-scoring
	# if state==1, this is post-scoring

	# score the red switch (on the left)
    if ($REDswitchL > $BLUEswitchL) {
		# RED owns its own switch
		$redOwnSw++;
		$REDscore += 5;
		$REDscore += 5 if ($round == 1);  # extra for autonomous
		if ("$redboostUp" == "1") {
			# boost activated and switch owned; double the score for
			# this portion of ownership
			$REDscore += 5;
		}
	} elsif ("$redforceUp" == "1" && ($REDforce == 1 || $REDforce == 3)) {
		# force activated and switch not owned; own it for this portion of
		# ownership
		$redOwnSw++;
		$REDscore += 5;
    }

	# score the scale
    if ($REDscale > $BLUEscale) {
		# RED owns the scale
		$redOwnSc++;
		$REDscore += 5;
		$REDscore += 5 if ($round == 1);  # extra for autonomous
		# check PowerUps
		if ("$blueforceUp" == "1" && ($BLUEforce == 2 || $BLUEforce == 3)) {
			# 20-point swing if BLUE force is activated
			$redOwnSc--;
			$REDscore -= 5;
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
		$BLUEscore += 5;
		$BLUEscore += 5 if ($round == 1); # extra for autonomous
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

	# score the blue switch (on the right)
    if ($REDswitchR < $BLUEswitchR) {
		# BLUE owns its own switch
		$bluOwnSw++;
		$BLUEscore += 5;
		$BLUEscore += 5 if ($round == 1); # extra for autonomous
		if ("$blueboostUp" == "1") {
			# boost activated and switch owned; double the score for
			# this portion of ownership
			$BLUEscore += 5;
		}
	} elsif ("$blueforceUp" == "1" && ($BLUEforce == 1 || $BLUEforce == 3)) {
		# force activated and switch not owned; own it for this portion of
		# ownership
		$bluOwnSw++;
		$BLUEscore += 5;

    }
}

sub scoreRedRobot($) {
    my ($action) = (@_);

    $REDswitchL++ if ($action == 1);
    $REDscale++   if ($action == 2);
    $REDswitchR++ if ($action == 3);


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

sub scoreBlueRobot($) {
    my ($action) = (@_);

    $BLUEswitchR++ if ($action == 1);
    $BLUEscale++   if ($action == 2);
    $BLUEswitchL++ if ($action == 3);


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

# check if cubes were taken from an empty location
sub emptycheck() {
	# check RED
	if ($pyramidL < 0) {
		# cannot take from empty pyramid so take from switch or portal
		$pyramidL = 0;
		# try taking from switch
		if ($switchL > 0) {
			$switchL--;
		} else {
			# portal is all that's left
			$REDportal--;
		}
	}
	if ($switchL < 0) {
		# cannot take from from switch so take from pyramid or portal
		$switchL = 0;
		# try taking from pyramid
		if ($pyramidL > 0) {
			$pyramidL--;
		} else {
			# portal is all that's left
			$REDportal--;
		}
	}
	if ($REDportal < 0) {
		# cannot take from from portal so take from pyramid or switch
		$REDportal = 0;
		# try taking from pyramid
		if ($pyramidL > 0) {
			$pyramidL--;
		} else {
			# switch is all that's left
			$switchL--;
		}
	}
	# now check BLUE
	if ($pyramidR < 0) {
		# cannot take from empty pyramid so take from switch or portal
		$pyramidR = 0;
		# try taking from switch
		if ($switchR > 0) {
			$switchR--;
		} else {
			# portal is all that's left
			$BLUEportal--;
		}
	}
	if ($switchR < 0) {
		# cannot take from from switch so take from pyramid or portal
		$switchR = 0;
		# try taking from pyramid
		if ($pyramidR > 0) {
			$pyramidR--;
		} else {
			# portal is all that's left
			$BLUEportal--;
		}
	}
	if ($BLUEportal < 0) {
		# cannot take from from portal so take from pyramid or switch
		$BLUEportal = 0;
		# try taking from pyramid
		if ($pyramidR > 0) {
			$pyramidR--;
		} else {
			# switch is all that's left
			$switchR--;
		}
	}
}

# remove cubes from locations
sub removeCubes($$) {
    my ($robot, $color) = (@_);
    $pyramidL-- if ("$color" eq "red" && $robot == 1);
	emptycheck();
    $switchL-- if ("$color" eq "red" && $robot == 2);
	emptycheck();
    $pyramidR-- if ("$color" eq "blue" && $robot == 1);
	emptycheck();
    $switchR-- if ("$color" eq "blue" && $robot == 2);
	emptycheck();
    $REDportal-- if ("$color" eq "red" && $robot == 3 && $REDportal > 0);
	emptycheck();
    $BLUEportal-- if ("$color" eq "blue" && $robot == 3 && $BLUEportal > 0);
	emptycheck();
}

sub printCube($) {
	my ($cubepos) = (@_);
	print "<div style=\"position:absolute; $cubepos\"><IMG SRC=cube.png></div>\n"
}

sub printTableLine($) {
	my ($multiplier) = (@_);
	my $a = $redOwnSw * $multiplier;
	my $b = $redOwnSc * $multiplier;
	my $c = $bluOwnSc * $multiplier;
	my $d = $bluOwnSw * $multiplier;
	
	my $redf = $REDforce * 5;
	my $redl = $REDlevitate * 5;
	my $redb = $REDboost * 5;
	my $bluf = $BLUEforce * 5;
	my $blul = $BLUElevitate * 5;
	my $blub = $BLUEboost * 5;
		
	$redf = "X" if ($REDforce > 3);
	$redl = "X" if ($REDlevitate > 3);
	$redb = "X" if ($REDboost > 3);
	$bluf = "X" if ($BLUEforce > 3);
	$blul = "X" if ($BLUElevitate > 3);
	$blub = "X" if ($BLUEboost > 3);
	
	my $x = "<tr><td align=center>$redf</td><td align=center>$redl</td><td align=center>$redb</td><td align=center>$a</td><td align=center>$b</td>\n";
	$x .= "<td align=center>$c</td><td align=center>$d</td><td align=center>$bluf</td><td align=center>$blul</td><td align=center>$blub</td></tr>\n";
	return $x;
}

# only score if $turn > 2
$turn++;

if ($turn > 2) {
	# process previous game results here
	
	# increment the round
	$round += 1;

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


	# process latest robot actions after both alliances have submitted
	# actions. ownership is calculated twice (before and after action)
	# with half-score each to split scoring on a change of ownership
	scoreOwnership(0);
	scoreRedRobot($R1);
	scoreRedRobot($R2);
	scoreRedRobot($R3);
	scoreBlueRobot($B1);
	scoreBlueRobot($B2);
	scoreBlueRobot($B3);
	scoreOwnership(1);

	removeCubes($RC1, "red");
	removeCubes($RC2, "red");
	removeCubes($RC3, "red");
	removeCubes($BC1, "blue");
	removeCubes($BC2, "blue");
	removeCubes($BC3, "blue");
	
	# reset the 'turn' to red for the next round
	$turn = 1;
	
	# update the scoring table
	$round0x = printTableLine(10) if ($round == 1);
	$round1x = printTableLine(5)  if ($round == 2);
	$round2x = printTableLine(5)  if ($round == 3);
	$round3x = printTableLine(5)  if ($round == 4);
	$round4x = printTableLine(5)  if ($round == 5);
	$round5x = printTableLine(5)  if ($round == 6);
	$round6x = printTableLine(5)  if ($round == 7);
	$round7x = printTableLine(5)  if ($round == 8);
	$round8x = printTableLine(5)  if ($round == 9);
	$round9x = printTableLine(5)  if ($round == 10);

	# process the powerups
	
	if ($redboostUp > 0) {
		$redboostUp = 2;
		$REDboost++ if ($REDboost == 3);
	}
	if ($redliftUp > 0) {
		$redliftUp = 2;
		$REDlevitate++ if ($REDlevitate == 3);
	}
	if ($redforceUp > 0) {
		$redforceUp = 2;
		$REDforce++ if ($REDforce == 3);
	}
	if ($blueboostUp > 0) {
		$blueboostUp = 2;
		$BLUEboost++ if ($BLUEboost == 3);
	}
	if ($blueliftUp > 0) {
		$blueliftUp = 2;
		$BLUElevitate++ if ($BLUElevitate == 3);
	}
	if ($blueforceUp > 0) {
		$blueforceUp = 2;
		$BLUEforce++ if($BLUEforce == 3);
	}
}

#
# Print the web page
#
print "Content-type: text/html\n\n";
print "<html><head>\n";
print "<title>FIRST Power Up!</title>\n";
print "<link rel='SHORTCUT ICON' href='favicon.ico'>\n";
print "<link rel='apple-touch-icon' href='favicon.png'>\n";
print "<meta name='description' content='FIRST Robotics Team 1073, Power Up Strategy Game'>\n";
print "<meta name='keywords' content='FIRST, Robotics, 1073, The Force Team, Po\
wer Up, Strategy Game'>\n";
print "<meta name='author' content='FIRST Team 1073'>\n";
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n";
print "</head>\n";
print "<body><center>\n";
print "<H1><I>FIRST</I> PowerUp! Strategy Game</H1>\n";

#
# print the updated game and the form with the new form
#
print "<FORM METHOD=\"post\" ACTION=\"alliance.cgi\">\n";
print "<input type=\"hidden\" name=\"REDforce\" value=\"$REDforce\">\n";        # number of RED force cubes 0-3(4 = activated)
print "<input type=\"hidden\" name=\"REDlevitate\" value=\"$REDlevitate\">\n";  # number of RED levitate cubes 0-3(4 = activated)
print "<input type=\"hidden\" name=\"REDboost\" value=\"$REDboost\">\n";        # number of RED boost cubes 0-3(4 = activated)
print "<input type=\"hidden\" name=\"BLUEportal\" value=\"$BLUEportal\">\n";    # number of BLUE portal cubes 0-11
print "<input type=\"hidden\" name=\"REDrobot1\" value=\"$REDrobot1\">\n";      # RED robot 1 cube (1 to start)
print "<input type=\"hidden\" name=\"REDrobot2\" value=\"$REDrobot2\">\n";      # RED robot 2 cube (1 to start)
print "<input type=\"hidden\" name=\"REDrobot3\" value=\"$REDrobot3\">\n";      # RED robot 3 cube (1 to start)
print "<input type=\"hidden\" name=\"pyramidL\" value=\"$pyramidL\">\n";        # number of RED pyramid cubes (0-10)
print "<input type=\"hidden\" name=\"REDswitchL\" value=\"$REDswitchL\">\n";    # number of cubes on L switch RED plate
print "<input type=\"hidden\" name=\"BLUEswitchL\" value=\"$BLUEswitchL\">\n";  # number of cubes on L switch BLUE plate
print "<input type=\"hidden\" name=\"switchL\" value=\"$switchL\">\n";          # number of cubes at L switch (0-6)
print "<input type=\"hidden\" name=\"REDscale\" value=\"$REDscale\">\n";        # number of cubes on RED scale plate
print "<input type=\"hidden\" name=\"BLUEscale\" value=\"$BLUEscale\">\n";      # number of cubes on BLUE scale plate
print "<input type=\"hidden\" name=\"switchR\" value=\"$switchR\">\n";          # number of cubes at R switch (0-6)
print "<input type=\"hidden\" name=\"REDswitchR\" value=\"$REDswitchR\">\n";    # number of cubes on R switch RED plate
print "<input type=\"hidden\" name=\"BLUEswitchR\" value=\"$BLUEswitchR\">\n";  # number of cubes on R switch BLUE plate
print "<input type=\"hidden\" name=\"pyramidR\" value=\"$pyramidR\">\n";        # number of BLUE pyramid cubes (0-10)    
print "<input type=\"hidden\" name=\"BLUErobot1\" value=\"$BLUErobot1\">\n";    # BLUE robot 1 cube (1 to start)                                                                             
print "<input type=\"hidden\" name=\"BLUErobot2\" value=\"$BLUErobot2\">\n";    # BLUE robot 2 cube (1 to start)                                                                             
print "<input type=\"hidden\" name=\"BLUErobot3\" value=\"$BLUErobot3\">\n";    # BLUE robot 3 cube (1 to start)                                                                             
print "<input type=\"hidden\" name=\"REDportal\" value=\"$REDportal\">\n";      # number of RED portal cubes 0-11                                                                            
print "<input type=\"hidden\" name=\"BLUEforce\" value=\"$BLUEforce\">\n";      # number of BLUE force cubes 0-3(4 = activated)                                                              
print "<input type=\"hidden\" name=\"BLUElevitate\" value=\"$BLUElevitate\">\n";# number of BLUE levitate cubes 0-3(4 = levitate)                                                            
print "<input type=\"hidden\" name=\"BLUEboost\" value=\"$BLUEboost\">\n";      # number of BLUE boost cubes 0-3(4 = activated)                                                               
print "<input type=\"hidden\" name=\"round\" value=\"$round\">\n";              # timed round number                                                                                         
print "<input type=\"hidden\" name=\"REDscore\" value=\"$REDscore\">\n";        # RED score    
print "<input type=\"hidden\" name=\"BLUEscore\" value=\"$BLUEscore\">\n";      # BLUE score
print "<input type=\"hidden\" name=\"turn\" value=\"$turn\">\n";				# who's turn?   
# need to preserve the red alliance movements past blue's turn
if ($turn > 1) {
	print "<input type=\"hidden\" name=\"R1\" value=\"$R1\">\n";
	print "<input type=\"hidden\" name=\"R2\" value=\"$R2\">\n";
	print "<input type=\"hidden\" name=\"R3\" value=\"$R3\">\n";
	print "<input type=\"hidden\" name=\"RC1\" value=\"$RC1\">\n";
	print "<input type=\"hidden\" name=\"RC2\" value=\"$RC2\">\n";
	print "<input type=\"hidden\" name=\"RC3\" value=\"$RC3\">\n";
}
print "<input type=\"hidden\" name=\"redforceUp\" value=\"$redforceUp\">\n";
print "<input type=\"hidden\" name=\"redboostUp\" value=\"$redboostUp\">\n";
print "<input type=\"hidden\" name=\"redliftUp\" value=\"$redliftUp\">\n";
print "<input type=\"hidden\" name=\"blueforceUp\" value=\"$blueforceUp\">\n";
print "<input type=\"hidden\" name=\"blueboostUp\" value=\"$blueboostUp\">\n";
print "<input type=\"hidden\" name=\"blueliftUp\" value=\"$blueliftUp\">\n";


print "<input type=\"hidden\" name=\"round0x\" value=\"$round0x\">\n";
print "<input type=\"hidden\" name=\"round1x\" value=\"$round1x\">\n";
print "<input type=\"hidden\" name=\"round2x\" value=\"$round2x\">\n";
print "<input type=\"hidden\" name=\"round3x\" value=\"$round3x\">\n";
print "<input type=\"hidden\" name=\"round4x\" value=\"$round4x\">\n";
print "<input type=\"hidden\" name=\"round5x\" value=\"$round5x\">\n";
print "<input type=\"hidden\" name=\"round6x\" value=\"$round6x\">\n";
print "<input type=\"hidden\" name=\"round7x\" value=\"$round7x\">\n";
print "<input type=\"hidden\" name=\"round8x\" value=\"$round8x\">\n";
print "<input type=\"hidden\" name=\"round9x\" value=\"$round9x\">\n";


# print the field
print "<table cellspacing=0 cellpadding=0 border=0><tr><td colspan=2>\n";
print "<div style=\"position:relative; background:url(field.png); no-repeat left top; width: 917px; height:477px;\">\n";

#switch/scale scoring                                                                          
print "<div style=\"position:absolute; top:132px; left:290px; color:yellow;\"><B>$REDswitchL</B></div>\n";
print "<div style=\"position:absolute; top:242px; left:290px; color:yellow;\"><B>$BLUEswitchL</B></div>\n";
print "<div style=\"position:absolute; top:115px; left:445px; color:yellow;\"><B>$BLUEscale</B></div>\n";
print "<div style=\"position:absolute; top:260px; left:445px; color:yellow;\"><B>$REDscale</B></div>\n";
print "<div style=\"position:absolute; top:132px; right:310px; color:yellow;\"><B>$REDswitchR</B></div>\n";
print "<div style=\"position:absolute; top:242px; right:310px; color:yellow;\"><B>$BLUEswitchR</B></div>\n";

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

if ($round == 0) {
	printCube($REDrobotPos1);
	printCube($REDrobotPos2);
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

if ($round == 0) {
	printCube($BLUErobotPos1);
	printCube($BLUErobotPos2);
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
$time = "2:15" if ($round == 1);
$time = "2:05" if ($round == 2);
$time = "1:55" if ($round == 3);
$time = "1:45" if ($round == 4);
$time = "1:35" if ($round == 5);
$time = "1:25" if ($round == 6);
$time = "1:15" if ($round == 7);
$time = "1:05" if ($round == 8);
$time = ":55"  if ($round == 9);
$time = ":00"  if ($round == 10);
print "</th><th>Time: $time</th><th>\n";
print "<H3><div style=\"color:blue\">Blue Alliance: $BLUEscore</div></H3>\n";
print "</tr></table></td></tr>\n";


#
# Helper functions for displaying the selections
#

# ex. printFrom("Red", "1", $REDpyramid, $REDswitch, $REDportal)
sub printFrom ($$$$) {
	my ($cube, $pyramid, $switch, $portal) = (@_);
	
	my $fchecked = "CHECKED=yes";
	my $lchecked = "";
	my $bchecked = "";
	$lchecked = "CHECKED=yes" if ($pyramid < 1);
	$bchecked = "CHECKED=yes" if ($pyramid < 1 && $switch < 1);
	print "<table cellpadding=0 cellspacing=0 border=0><tr><td>\n";
	print "<INPUT TYPE=\"radio\" NAME=\"$cube\" VALUE=\"1\" $fchecked>pyramid<br>\n"     if ($pyramid > 0);
	print "<INPUT TYPE=\"radio\" NAME=\"$cube\" VALUE=\"2\" $lchecked>switch edge<br>\n" if ($switch > 0);
	print "<INPUT TYPE=\"radio\" NAME=\"$cube\" VALUE=\"3\" $bchecked>portal\n"          if ($portal > 0);
	print "</td></tr></table>\n";
}

# ex. printTo("R1", "RED", $REDforce, $REDlevitate, $REDboost)
sub printTo($$$$$) {
	my ($robot, $color, $force, $levitate, $boost) = (@_);

	print "<table><tr><td>";	
	print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"1\" CHECKED=yes>$color plate on own SWITCH<br>\n";
	print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"2\" >$color plate on SCALE<br>\n";
	print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"3\" >$color plate on opposing SWITCH<br>\n" if ($round > 0);
	print "</td><td>";
	if ($force < 3) {
		print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"4\">exchange/vault for Force<br>\n";
	} else {
		print "&nbsp;<br>\n";
	}
	if ($levitate < 3) {
		print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"5\">exchange/vault for Levitate<br>\n";
	} else {
		print "&nbsp;<br>\n";
	}
	if ($boost < 3) {
		print "<INPUT TYPE=\"radio\" NAME=\"$robot\" VALUE=\"6\">exchange/vault for Boost<br>\n";
	} else {
		print "&nbsp;<br>\n";
	}
	print "</td></tr></table>\n";
}

sub printPowerUps($$$$$$$) {
	my ($color, $force, $levitate, $boost, $fup, $lup, $bup) = (@_);
	
	print "</td></tr><tr><td colspan=2 align=center>\n";
	my $space = "&nbsp;&nbsp;&nbsp;&nbsp;";
	print "<INPUT TYPE=\"checkbox\" NAME=\"${color}fUp\" VALUE=\"1\">Force Up!$space\n"   if ($fup == 0 && $force > 0 && $force < 4);
	print "<INPUT TYPE=\"checkbox\" NAME=\"${color}lUp\" VALUE=\"1\">Levitate Up!$space\n" if ($lup == 0 && $levitate > 0 && $levitate < 4);
	print "<INPUT TYPE=\"checkbox\" NAME=\"${color}bUp\" VALUE=\"1\">Boost Up!$space\n"   if ($bup == 0 && $boost > 0 && $boost < 4);
	print "&nbsp;\n" if (($force < 1 || $force > 3) && ($levitate < 1 || $levitate > 3) && ($boost < 1 || $boost > 3));
}

if ($round < 10) {
	#
	# Print 
	#
	for (my $n = 1; $n < 4; $n++) {
		print "<tr><td colspan=2 align=center>\n";
		print "<table border=1><tr><td><table><tr><td align=center>";
		if ($turn == 1) {
			if ($round == 0) {
				print "<p><b>Red Robot #${n}</b> delivers its cube to the:&nbsp;\n";
			} else {
				print "<table><tr><td>";
				print "<p><b>Red #${n} from</b>";
				print "</td><td>";
				printFrom("RC${n}", $pyramidL, $switchL, $REDportal);
				print "</td><td>";
				print "&nbsp;<b>to</b>&nbsp;";
				print "</td></tr></table>";
			}
			print "</td><td align=center>\n";
			printTo("R${n}", "RED", $REDforce, $REDlevitate, $REDboost);
		} else {
			if ($round == 0) {
				print "<p><b>Blue Robot #${n}</b> delivers its cube to the:&nbsp;\n";
			} else {
				print "<table><tr><td>";
				print "<p><b>Blue #${n} from</b><br>";
				print "</td><td>";
				printFrom("BC${n}", $pyramidR, $switchR, $BLUEportal);
				print "</td><td>";
				print "&nbsp;<b>to</b>&nbsp;";
				print "</td></tr></table>";
			}
			print "</td><td>\n";
			printTo("B${n}", "BLUE", $BLUEforce, $BLUElevitate, $BLUEboost);
		}
		print "</td></tr></table></td></tr></table>";
		print "</td></tr>\n";
	}

	if ($turn == 1) {
		printPowerUps("red", $REDforce, $REDlevitate, $REDboost, $redforceUp, $redliftUp, $redboostUp);
	} else {
		printPowerUps("blue", $BLUEforce, $BLUElevitate, $BLUEboost, $blueforceUp, $blueliftUp, $blueboostUp);
	}

	print "</td></tr><tr>";
	print "<td colspan=2 align=center><p><br>\n";
	print "<input type=\"submit\" value=\"Submit Selections\">\n";
	print "</p></tr>";
} else {
	print "<tr><td colspan=2 align=center>THE END</td></tr>\n";
}
print "</table>\n";
print "<p>&nbsp;</p>\n";

print "<table border=1>\n";
print "<tr><td align=center colspan=5>RED</th><th align=center colspan=5>BLUE</th></tr>\n";
print "<tr><th>force</th><th>levitate</th><th>boost</th><th>SWITCH</th><th>SCALE</th>\n";
print "<th>SCALE</th><th>SWITCH</th><th>force</th><th>levitate</th><th>boost</th></tr>\n";
print "$round0x\n";
print "$round1x\n";
print "$round2x\n";
print "$round3x\n";
print "$round4x\n";
print "$round5x\n";
print "$round6x\n";
print "$round7x\n";
print "$round8x\n";
print "$round9x\n";
print "</table>\n";

# add debugging
if ($debug) {
	print "<H5>Debug info</H5>\n";
	print "<p>turn = $turn</p>\n";
	print "<p>round = $round</p>\n";
	print "<p>R1 = $R1, B1 = $B1</p>\n";
	print "<p>R2 = $R2, B2 = $B2</p>\n";
	print "<p>R3 = $R3, B3 = $B3</p>\n";
	print "<p>REDforce = $REDforce, BLUEforce = $BLUEforce</p>\n";
	print "<p>REDlevitate = $REDlevitate, BLUElevitate = $BLUElevitate</p>\n";
	print "<p>REDboost = $REDboost, BLUEboost = $BLUEboost</p>\n";
	print "<p>redforceUp = $redforceUp, blueforceUp = $blueforceUp</p>\n";
	print "<p>redliftUp = $redliftUp, blueliftUp = $blueliftUp</p>\n";
	print "<p>redboostUp = $redboostUp, blueboostUp = $blueboostUp</p>\n";
	print "<p>pyramidL = $pyramidL, pyramidR = $pyramidR</p>\n";
	print "<p>switchL = $switchL, switchR = $switchR</p>\n";
	print "<p>REDportal = $REDportal, BLUEportal = $BLUEportal</p>\n";
	
}

print "</BODY></HTML>\n";


