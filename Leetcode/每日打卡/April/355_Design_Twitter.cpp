/*
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.

Example:
Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

// !!!!!!!!UNSOVLED

class Twitter {
private:
    unordered_map<int, unordered_set<int>> user_followings;
    vector<pair<int, int>> tweets;
public:
    /** Initialize your data structure here. */
    Twitter() {
        
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        if(user_followings.count(userId)==0){
            user_followings.insert({userId, unordered_set<int> {userId}});
        }
        tweets.push_back({userId, tweetId});
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> feeds;
        int max_num = 10, cur_pos = tweets.size()-1;
        if(user_followings.count(userId)==0) return feeds;
        unordered_set<int> followings = user_followings[userId];
        while (max_num > 0 && cur_pos >= 0) 
        {
            if(followings.count(tweets[cur_pos].first)!=0) {
                feeds.push_back(tweets[cur_pos].second);
                max_num--;
            }
            cur_pos--;
        }
        return feeds;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        if(user_followings.count(followerId)==0){
            user_followings.insert({followerId, unordered_set<int> {followerId}});
        }
        user_followings[followerId].insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        if(followerId != followeeId)
            user_followings[followerId].erase(followeeId);
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */

int main(){
    Twitter twitter = Twitter();

    twitter.postTweet(11,994);
    twitter.postTweet(4,303);
    twitter.postTweet(1,113);
    twitter.postTweet(18,309);
    twitter.postTweet(8,905);
    twitter.postTweet(6,605);
    twitter.postTweet(1,210);
    twitter.postTweet(15,15);
    twitter.postTweet(1,88);
    twitter.postTweet(1,704);
    twitter.getNewsFeed(8);
    twitter.postTweet(9,59);
    twitter.postTweet(4,851);
    twitter.postTweet(13,974);
    twitter.postTweet(2,133);
    twitter.postTweet(15,255);
    twitter.postTweet(15,662);
    twitter.postTweet(16,21);
    twitter.postTweet(13,227);
    twitter.getNewsFeed(17);
    twitter.postTweet(5,603);
    twitter.unfollow(10,7);
    twitter.postTweet(5,816);
    twitter.postTweet(7,792);
    twitter.postTweet(12,260);
    twitter.getNewsFeed(5);
    twitter.postTweet(4,586);
    twitter.postTweet(1,645);
    twitter.getNewsFeed(20);
    twitter.postTweet(15,171);
    twitter.postTweet(16,18);
    twitter.postTweet(3,812);
    twitter.postTweet(15,153);
    twitter.postTweet(12,726);
    twitter.postTweet(6,508);
    twitter.postTweet(17,817);
    twitter.follow(5,6);
    twitter.postTweet(3,667);
    twitter.postTweet(5,599);
    twitter.postTweet(13,353);
    twitter.postTweet(11,282);
    twitter.postTweet(7,226);
    twitter.postTweet(18,423);
    twitter.postTweet(13,875);
    twitter.postTweet(2,738);
    twitter.postTweet(6,727);
    twitter.postTweet(7,374);
    twitter.postTweet(19,811);
    twitter.postTweet(8,418);
    twitter.postTweet(2,179);
    twitter.postTweet(3,476);
    twitter.follow(9,15);
    twitter.postTweet(16,8);
    twitter.postTweet(19,827);
    twitter.postTweet(17,203);
    twitter.postTweet(13,246);
    twitter.follow(14,8);
    twitter.postTweet(13,750);
    twitter.postTweet(4,595);
    twitter.postTweet(1,793);
    twitter.postTweet(17,995);
    twitter.postTweet(11,589);
    twitter.postTweet(2,115);
    twitter.postTweet(18,870);
    twitter.postTweet(15,426);
    twitter.postTweet(18,953);
    twitter.postTweet(10,318);
    twitter.postTweet(10,419);
    twitter.postTweet(2,164);
    twitter.getNewsFeed(9);
    twitter.postTweet(18,854);
    twitter.postTweet(3,394);
    vector<int> res = twitter.getNewsFeed(17);
    return 0;
}