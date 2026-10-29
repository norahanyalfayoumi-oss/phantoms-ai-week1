def process_team_scores(scores_list):
    
    total_score = 0
    passed_members = []
    valid_count = 0
    
    for score in scores_list:
        try:
    
            numeric_score = float(score)
            
            total_score += numeric_score
            valid_count += 1
            
            
            # التصحيح: استخدام أكبر من أو يساوي 50 للنجاح
            if numeric_score >= 50:
                passed_members.append(numeric_score)
                
        except ValueError:
            print(f"تحذير: تم تجاهل قيمة غير صالحة ({score})")
            
    # حماية البرنامج من القسمة على صفر
    if valid_count == 0:
        return 0, []
        
    average = total_score / valid_count
    return average, passed_members

# تجربة الدالة على بيانات اختبار
sample_scores = [45, 50, 75, 90, 60]
avg, passed = process_team_scores(sample_scores)
print(f"Average: {avg}, Passed: {passed}")