import System.IO
import Data.Char (isNumber, digitToInt)
import Data.List (isInfixOf, isPrefixOf)
import Data.Maybe (mapMaybe)

processLineP1 :: String -> Int
processLineP1 line =
  let firstDigit = head $ filter isNumber line
      lastDigit = last $ filter isNumber line 
  in
  10 * (digitToInt firstDigit) + (digitToInt lastDigit)

processLinesP1 :: [String] -> Int
processLinesP1 lines = sum $ map processLineP1 lines

digitsL :: [(String, Int)] = [("one", 1), ("two", 2), ("three", 3), ("four", 4),
        ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]
digitsL' :: [(String, Int)] = [("eno", 1), ("owt", 2), ("eerht", 3), ("ruof", 4),
        ("evif", 5), ("xis", 6), ("neves", 7), ("thgie", 8), ("enin", 9)]
          

digitOrWord :: String -> [(String, Int)] -> Int
digitOrWord [] digits = 0
digitOrWord (x:xs) digits =
  case mapMaybe (\(word, num) -> if word `isPrefixOf` (x:xs) then Just num else Nothing) digits of
    (num:_) -> num
    [] ->
       if isNumber x then read [x] 
       else digitOrWord xs digits

isInString :: String -> String -> Bool
isInString str substr = substr `isInfixOf` str

-- try to find a member of digitsL in the string and if so run digToInt on it
processLineP2 :: String -> Int
processLineP2 line =
  let firstDigit = digitOrWord line digitsL
      lastDigit = digitOrWord (reverse line) digitsL'
  in
  10 * firstDigit + lastDigit

processLinesP2 :: [String] -> Int
processLinesP2 lines = sum $ map processLineP2 lines

main :: IO ()
main = do
  -- Open file for reading
  handle <- openFile "input" ReadMode
  -- Read contents of into a list of lines
  -- (each line is one element of the list)
  contents <- hGetContents handle
  -- Get the sum of processLines
  putStrLn $ show $ processLinesP1 $ lines contents
  putStrLn $ show $ processLinesP2 $ lines contents
