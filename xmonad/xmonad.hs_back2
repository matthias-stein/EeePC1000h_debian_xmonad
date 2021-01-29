-- XMonad
import XMonad

-- XMonad.Actions
import XMonad.Actions.CycleWS
import XMonad.Actions.UpdatePointer

-- XMonad.Hooks
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.FadeInactive
import XMonad.Hooks.ManageDocks

-- XMonad.Layout
import XMonad.Layout.BinarySpacePartition
import XMonad.Layout.Grid
import XMonad.Layout.LimitWindows (limitWindows)
import XMonad.Layout.NoBorders
import XMonad.Layout.Renamed (renamed, Rename(Replace))
import XMonad.Layout.ResizableTile
import XMonad.Layout.Spacing
import XMonad.Layout.ThreeColumns

-- XMonad.Util
import XMonad.Util.EZConfig
import XMonad.Util.SpawnOnce
import XMonad.Util.Run

-- Data
import Data.Monoid
import Data.Maybe (isJust)

-- System
import System.IO (hPutStrLn)
import System.Exit

-- Qualified imports
import qualified XMonad.StackSet as W
import qualified Data.Map        as M

-- The preferred terminal program, which is used in a binding below and by
-- certain contrib modules.
--
-- myTerminal      = "urxvtc"  -- start client, see MySartupHook for daemon
myTerminal      = "st"  

-- Whether focus follows the mouse pointer.
myFocusFollowsMouse :: Bool
myFocusFollowsMouse = True

-- Whether clicking on a window to focus also passes the click to the window
myClickJustFocuses :: Bool
myClickJustFocuses = False

-- Width of the window border in pixels.
--
myBorderWidth   = 2

-- modMask lets you specify which modkey you want to use. The default
-- is mod1Mask ("left alt").  You may also consider using mod3Mask
-- ("right alt"), which does not conflict with emacs keybindings. The
-- "windows key" is usually mod4Mask.
--
myModMask       = mod4Mask

-- The default number of workspaces (virtual screens) and their names.
-- By default we use numeric strings, but any string may be used as a
-- workspace name. The number of workspaces is determined by the length
-- of this list.
--
-- A tagging example:
--
-- > workspaces = ["web", "irc", "code" ] ++ map show [4..9]
--
myWorkspaces    = ["1","2","3","4","5","6","7","8","9"]

-- Border colors for unfocused and focused windows, respectively.
--
myNormalBorderColor  = "#b58900"
myFocusedBorderColor = "#d33682"

-- number of windows on workspace
windowCount :: X (Maybe String)
windowCount = gets $ Just . show . length . W.integrate' . W.stack . W.workspace . W.current . windowset


------------------------------------------------------------------------
-- Key bindings. Add, modify or remove key bindings here.
--
-- https://hackage.haskell.org/package/xmonad-contrib-0.16/docs/XMonad-Util-EZConfig.html
myKeys = [
    ("M-S-<Return>", spawn myTerminal)  -- launch a terminal
  , ("M-p"         , spawn "dmenu_run -fn 'xft:Ubuntu Mono:size=11:bold:antialias=true' \
                              \-nb '#002b36' -nf '#839496' -sb '#b58900' -sf '#002b36'")  -- launch dmenu with solarized colors
  , ("M-S-p"       , spawn "gmrun")  -- launch gmrun
  , ("M-S-c"       , kill)  -- close focused window
  , ("M-<Space>"   , sendMessage NextLayout)  -- Rotate through the available layout algorithms
  -- , (("M-S-<Space>"), setLayout  $ XMonad.layoutHook conf )  --  Reset the layouts on the current workspace to default
  , ("M-n"         , refresh)  -- Resize viewed windows to the correct size
  , ("M-<Tab>"     , windows W.focusDown)  -- Move focus to the next window
  , ("M-j"         , windows W.focusDown)  -- Move focus to the next window
  , ("M-k"         , windows W.focusUp  )  -- Move focus to the previous window
  , ("M-m"         , windows W.focusMaster  )  -- Move focus to the master window
  , ("M-<Return>"  , windows W.swapMaster)  -- Swap the focused window and the master window
  , ("M-S-j"       , windows W.swapDown  )  -- Swap the focused window with the next window
  , ("M-S-k"       , windows W.swapUp    )  -- Swap the focused window with the previous window
  , ("M-h"         , sendMessage Shrink)  -- Shrink the master area
  , ("M-l"         , sendMessage Expand)  -- Expand the master area
  , ("M-t"         , withFocused $ windows .W.sink)  -- Push window back into tiling
  , ("M-,"         , sendMessage (IncMasterN 1))  -- Increment the number of windows in the master area
  , ("M-."         , sendMessage (IncMasterN (-1)))  -- Deincrement the number of windows in the master area
  , ("M-b"         , sendMessage ToggleStruts)  -- Toggle the status bar gap
  , ("M-S-q"       , io (exitWith ExitSuccess))  -- Quit xmonad
  , ("M-q"         , spawn "xmonad --recompile; xmonad --restart")   -- Restart xmonad
  , ("C-M1-<Up>"   , nextWS)  -- Shifts focused window to next ws
  , ("C-M1-<Down>" , prevWS)  -- Shifts focused window to prev ws

    ]
    -- ++ [(("M-" ++ k), windows $ i) | (i, k) <- zip(XMonad.workspaces myWorkspaces)] 
    -- ++

    --
    -- mod-[1..9], Switch to workspace N
    -- mod-shift-[1..9], Move client to workspace N
    --
    -- [((m .|. modm, k), windows $ f i)
    --     | (i, k) <- zip (XMonad.workspaces conf) [xK_1 .. xK_9]
    --    , (f, m) <- [(W.greedyView, 0), (W.shift, shiftMask)]]
    -- ++

    --
    -- mod-{w,e,r}, Switch to physical/Xinerama screens 1, 2, or 3
    -- mod-shift-{w,e,r}, Move client to screen 1, 2, or 3
    --
    -- [((m .|. modm, key), screenWorkspace sc >>= flip whenJust (windows . f))
    --     | (key, sc) <- zip [xK_w, xK_e, xK_r] [0..]
    --     , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]


------------------------------------------------------------------------
-- Mouse bindings: default actions bound to mouse events
--
myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList $

    -- mod-button1, Set the window to floating mode and move by dragging
    [ ((modm, button1), (\w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster))

    -- mod-button2, Raise the window to the top of the stack
    , ((modm, button2), (\w -> focus w >> windows W.shiftMaster))

    -- mod-button3, Set the window to floating mode and resize by dragging
    , ((modm, button3), (\w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster))

    -- you may also bind events to the mouse scroll wheel (button4 and button5)
    ]

------------------------------------------------------------------------
-- Layouts:
-- https://betweentwocommits.com/blog/xmonad-layouts-guide
--
myLayout = avoidStruts ( full ||| tall ||| mtll ||| col3 ||| grid )
  where
     -- full - one window uses all of screen, no border
     full = renamed [Replace "Full"] 
          $ limitWindows 1
          $ noBorders (Full)

     -- tall - master/stack layout
     tall = renamed [Replace "Tall"] 
          $ spacingRaw True (Border 5 0 5 0) True (Border 0 5 0 5) True 
          $ ResizableTall 1 (3/100) (1/2) []

     -- mtll - the tall layout rotatet 90°
     mtll = Mirror tall

     -- col3 - three column layout
     col3 = renamed [Replace "Col3"]
          $ limitWindows 3
          $ spacingRaw True (Border 2 2 2 2) True (Border 2 2 2 2) True
          $ ThreeCol 1 (3/100) (1/3)

     -- grid - all windows distributed as evenly as possible
     grid = renamed [Replace "Grid"]
          $ limitWindows 12
          $ spacingRaw True (Border 2 2 2 2) True (Border 2 2 2 2) True
          $ GridRatio (4/3) 

     -- The default number of windows in the master pane
     nmaster = 1

     -- Default proportion of screen occupied by master pane
     ratio   = 1/2

     -- Percent of screen to increment by when resizing panes
     delta   = 3/100

------------------------------------------------------------------------
-- Window rules:

-- Execute arbitrary actions and WindowSet manipulations when managing
-- a new window. You can use this to, for example, always float a
-- particular program, or have a client always appear on a particular
-- workspace.
--
-- To find the property name associated with a program, use
-- > xprop | grep WM_CLASS
-- and click on the client you're interested in.
--
-- To match on the WM_NAME, you can use 'title' in the same way that
-- 'className' and 'resource' are used below.
--
myManageHook = composeAll
    [ className =? "MPlayer"        --> doFloat
    , className =? "Gimp"           --> doFloat
    , resource  =? "desktop_window" --> doIgnore
    , resource  =? "kdesktop"       --> doIgnore ]

------------------------------------------------------------------------
-- Event handling

-- * EwmhDesktops users should change this to ewmhDesktopsEventHook
--
-- Defines a custom handler function for X Events. The function should
-- return (All True) if the default handler is to be run afterwards. To
-- combine event hooks use mappend or mconcat from Data.Monoid.
--
myEventHook = mempty

------------------------------------------------------------------------
-- Status bars and logging

-- Perform an arbitrary action on each internal state change or X event.
-- See the 'XMonad.Hooks.DynamicLog' extension for examples.
--
-- myLogHook = return ()
-- myLogHook :: X ()
-- myLogHook = fadeInactiveLogHook fadeAmount
--     where fadeAmount = 1.0
myLogHook dest = dynamicLogWithPP xmobarPP { 
                     ppOutput          = hPutStrLn dest
                   , ppCurrent         = xmobarColor "#268bd2" "" . wrap "[" "]"  -- Visible&Focussed workspace in xmobar
                   , ppVisible         = xmobarColor "#93a1a1" "" . wrap "[" "]"  -- Visible but unfocussed workspace
                   , ppHidden          = xmobarColor "#93a1a1" "" . wrap "'" "'"  -- Hidden workspaces, 1+ windows
                   , ppHiddenNoWindows = xmobarColor "#93a1a1" "" . wrap " " " "  -- Hidden workspaces, no windows
                   , ppTitle           = xmobarColor "#859900" "" . shorten 60    -- Title of active window
                   , ppWsSep           = xmobarColor "#002b36" "" " "             -- Separator between workspaces
                   , ppSep             = xmobarColor "#839496" "" " | "           -- Separator between sections 
                   , ppUrgent          = xmobarColor "#d33682" "" . wrap "!" "!"  -- Urgent workspace
                   , ppExtras          = [windowCount]                            -- # of windows in focussed workspace
                   , ppOrder           = \(ws:l:t:ex) -> [ws,l]++ex++[t]
                 }
-- Perform an arbitrary action each time xmonad starts or is restarted
-- with mod-q.  Used by, e.g., XMonad.Layout.PerWorkspace to initialize
-- per-workspace layout choices.
--
-- By default, do nothing.
myStartupHook = do
    -- start compositor
    spawnOnce "compton &"
   
    -- start urxvt terminal daemon
    -- spawnOnce "urxvtd &" 

------------------------------------------------------------------------
-- Now run xmonad with all the defaults we set up.

-- Run xmonad with the settings you specify. No need to modify this.
--
main = do
    xmproc <- spawnPipe "xmobar ~/.config/xmobar/xmobarrc"
    xmonad $ docks $ def {
        manageHook         = myManageHook
      , startupHook        = myStartupHook
      , layoutHook         = myLayout
      , handleEventHook    = myEventHook 
      , workspaces         = myWorkspaces
      , borderWidth        = myBorderWidth
      , terminal           = myTerminal
      , modMask            = myModMask
      , normalBorderColor  = myNormalBorderColor
      , focusedBorderColor = myFocusedBorderColor
      , logHook            = myLogHook xmproc
    } `additionalKeysP` myKeys

