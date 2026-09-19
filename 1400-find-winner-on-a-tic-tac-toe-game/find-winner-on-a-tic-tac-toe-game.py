class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        # Store sums for each row, column, and two diagonals
        row = [0] * 3    # Sums for three rows
        col = [0] * 3    # Sums for three columns
        diag1 = 0        # Main diagonal (top-left to bottom-right)
        diag2 = 0        # Anti-diagonal (top-right to bottom-left)

        # Process each move in sequence
        for move_number in range(len(moves)):
            # Get current move coordinates
            rowIndex = moves[move_number][0]
            colIndex = moves[move_number][1]
            # Determine player: A (1) for even moves, B (-1) for odd moves
            player = 1 if move_number % 2 == 0 else -1

            # Update row and column sums
            row[rowIndex] += player
            col[colIndex] += player
            
            # Update main diagonal (if cell is on it)
            if rowIndex == colIndex:
                diag1 += player
            
            # Update anti-diagonal (if cell is on it)
            if rowIndex + colIndex == 2:
                diag2 += player
        
            # Check win conditions (sum of 3 or -3 in any direction)
            if (abs(row[rowIndex]) == 3 or # Row check
                abs(col[colIndex]) == 3 or # Column check
                abs(diag1) == 3 or         # Main diagonal
                abs(diag2) == 3):          # Anti-diagonal
                return 'A' if player == 1 else 'B'  # Return winner
        
        # No winner: Draw if board full (9 moves), else game continues
        return 'Draw' if len(moves) == 9 else 'Pending'