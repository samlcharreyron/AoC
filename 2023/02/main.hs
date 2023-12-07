import System.IO
import Data.Map (Map, fromList, (!?), insertWith, empty)
import qualified Data.Map as Map
import Data.Maybe (fromMaybe)
import Debug.Trace
-- import Data.Text (splitOn)
  --
type Bag = [(String, Int)]
data Game = Game { gid :: Int, bags :: [Bag] } deriving (Show)

splitBy :: Char -> String -> [String]
splitBy delimiter = foldr f [[]] 
    where
      f c l@(x:xs)
          | c == delimiter = []:l
          | otherwise = (c:x):xs

getTuple :: String -> (String, Int)
getTuple line = (last (words line), read $ head (words line)) 

getBagContents :: String -> Bag
getBagContents line =  map getTuple (splitBy ',' line)

getGame :: String -> Game
getGame line = Game { gid = game_num, bags = map getBagContents $ splitBy ';' bagS }
  where game_num = read $ last $ words (head (splitBy ':' line)) :: Int
        bagS =  last (splitBy ':' line)

isValidBag :: [(String, Int)] -> Bool
isValidBag bag = all isValid [("red", 12), ("green", 13), ("blue", 14)]
  where
      isValid (color, maxCount) = fromMaybe True $ fmap (<= maxCount) (lookup color bag)

isValidGame :: Game -> Bool
isValidGame game = all isValidBag (bags game)

part1 :: [String] -> Int
part1 lines = sum (map gid valid_games)
  where valid_games = filter isValidGame (map getGame lines)

insertCube :: (String, Int) -> Map String Int -> Map String Int
insertCube entry = insertWith max color num 
  where color = fst entry
        num = snd entry

insertCubes :: [Bag] -> Bag
insertCubes bags = Map.toList $ foldr insertCube empty (concat bags)

getCubeVal :: Bag -> Int
getCubeVal bag = product $ map snd bag

part2 :: [String] -> Int
part2 lines = sum cube_vals
  where 
    games = map getGame lines
    cube_vals :: [Int] = map ((getCubeVal . insertCubes) . bags) games

main :: IO ()
main = do
    handle <- openFile "input" ReadMode
    contents <- hGetContents handle
    let inp = lines contents
    print(part1 inp)
    print(part2 inp)
