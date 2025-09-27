class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # This is the value returned when index is out of bounds
        INF = 2**31 - 1

        # now lets find the search range, lets start with the small windows
        left, right = 0, 1

        # Expand the window until these 2 conditions:
        #  - we go out of bounds, OR
        #  - the value at 'right' is >= target
        while True:
            # this line checks the value at the current index
            val = reader.get(right)

            # If val is out of bounds (INF) or we already passed target
            if val == INF or val >= target:
                break  # stop expanding

            # Else we shift the window( M = middle point)  to the right
            left = right
            right <<= 1  # Right X 2 for exponetial growth

        # Now, lets perform binary serach [L,R]
        while left <= right:
            mid = (left + right) // 2  # midpoint of current window
            val = reader.get(mid)      # value at M 

            # Foudn the target
            if val == target:
                return mid

            # move right 
            if val == INF or val > target:
                right = mid - 1
            else:
                # If value is too small, move left up
                left = mid + 1

        # If we exit teh loop, target not found 
        return -1

      
  


  
      
